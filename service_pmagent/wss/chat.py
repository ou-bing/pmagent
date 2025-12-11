import logging
from typing import Literal, Optional, TypedDict
from urllib.parse import parse_qs

import orjson
from channels.auth import login
from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings
from django.contrib.auth.models import User
from jose import jwt
from langchain.chat_models import init_chat_model
from langchain_core.messages import BaseMessage, HumanMessage

from domains.im.models import Message, Session

logger = logging.getLogger(__name__)

model = init_chat_model(
    settings.CHAT_MODEL,
    temperature=0,
    base_url=settings.CHAT_MODEL_BASE_URL,
    api_key=settings.CHAT_MODEL_API_KEY,
)


class Payload(TypedDict):
    id: Optional[int]
    content: str
    role: Literal["human", "ai"]
    session_id: str


class Event(TypedDict):
    type: str
    payload: Payload


class AsyncChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        try:
            params = parse_qs(self.scope["query_string"].decode("utf-8"))
            token = params.get("token", [""])[0]
            payload = jwt.decode(
                token.replace("Bearer ", ""),
                settings.SECRET_KEY,
                algorithms=["HS256"],
            )
            user = await User.objects.aget(pk=payload["id"])
            await login(self.scope, user)
        except BaseException:
            logger.exception("ws connection error")
            return await self.close(401)

        self.room_name = self.scope["url_route"]["kwargs"]["session_id"]  # type: ignore
        self.room_group_name = f"session_{self.room_name}"

        if self.channel_layer:
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name,
            )

        await self.accept()

    async def disconnect(self, close_code):
        if self.channel_layer:
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name,
            )

    async def receive(self, text_data):
        p: Payload = orjson.loads(text_data)
        user_id = self.scope["user"].id  # type: ignore
        if not await Session.objects.filter(
            pk=p["session_id"],
            user_id=user_id,
        ).aexists():
            raise ValueError(
                f"Invalid payload, user: {user_id}, session: {p['session_id']}"
            )

        msg = await Message.objects.acreate(
            session_id=p["session_id"],
            user_id=user_id,
            role="human",
            body={"content": p["content"]},
        )
        p["id"] = msg.pk

        if self.channel_layer:
            await self.channel_layer.group_send(
                self.room_group_name,
                {"type": "session.message", "payload": p},
            )

    async def session_message(self, event):
        p: Payload = event["payload"]
        await self.send(text_data=orjson.dumps(p).decode("utf-8"))

        res: BaseMessage = await model.ainvoke(
            [
                HumanMessage(
                    content=p["content"],
                )
            ]
        )
        msg = await Message.objects.acreate(
            session_id=p["session_id"],
            user=self.scope["user"],  # type: ignore
            role=res.type,
            body={"content": str(res.content)},
        )
        await self.send(
            text_data=orjson.dumps(
                Payload(
                    id=msg.pk,
                    content=str(res.content),
                    role="ai",
                    session_id=p["session_id"],
                )
            ).decode("utf-8")
        )
