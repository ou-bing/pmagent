import logging

import orjson
from django.conf import settings
from django.http import HttpRequest, StreamingHttpResponse
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from ninja import Field, FilterSchema, ModelSchema, Query, Router, Schema

from domains.im.models import Message, Session
from domains.infra.django_ninja_utils import (
    JwtAuth,
    ListResponseSchema,
    ResponseSchema,
)

logger = logging.getLogger(__name__)

router = Router(auth=JwtAuth())


class CreateSessionReq(Schema):
    title: str = Field(
        default="",
    )


class CreateSessionRes(ModelSchema):
    class Meta:
        model = Session
        fields = "__all__"


class ListSessionRes(ModelSchema):
    class Meta:
        model = Session
        fields = "__all__"


class ListMessageReq(FilterSchema):
    session_id: int


class ListMessageRes(ModelSchema):
    class Meta:
        model = Message
        fields = "__all__"


class SseReq(Schema):
    content: str = Field(description="")
    session_id: int = Field(description="")


class SseRes(Schema):
    id: int = Field(description="")
    content: str = Field(description="")
    type: str = Field(description="")


@router.post(
    "/session",
    summary="",
    response={200: ResponseSchema[CreateSessionRes], 400: ResponseSchema},
)
def create_session(
    request: HttpRequest,
    data: CreateSessionReq,
):
    session = Session.objects.create(
        title=data.title,
        user_id=request.user.pk,
    )
    return ResponseSchema(data=session)


@router.get(
    "/session",
    summary="",
    response={200: ListResponseSchema[ListSessionRes], 400: ResponseSchema},
)
def list_sessions(
    request: HttpRequest,
    page: int = 1,
    size: int = 10,
):
    query = Session.objects.filter(user_id=request.user.pk)
    return ListResponseSchema.from_queryset(
        query,
        page,
        size,
    )


@router.get(
    "/message",
    summary="",
    response={200: ListResponseSchema[ListMessageRes], 400: ResponseSchema},
)
def list_messages(
    request: HttpRequest,
    filters: Query[ListMessageReq],
    page: int = 1,
    size: int = 10,
):
    query = Message.objects.filter(user_id=request.user.pk)
    return ListResponseSchema.from_queryset(
        filters.filter(query),
        page,
        size,
    )


@router.post(
    "/sse",
    summary="",
    response={200: SseRes, 400: ResponseSchema},
)
async def sse_stream(request: HttpRequest, data: SseReq):
    model = ChatOpenAI(
        model="gpt-5-nano",
        base_url=settings.CHAT_MODEL_BASE_URL,
        api_key=settings.CHAT_MODEL_API_KEY,
    )
    q_msg = await Message.objects.acreate(
        user_id=request.user.pk,
        body={"content": data.content},
        role=Message.Role.HUMAN,
        session_id=data.session_id,
    )

    async def event_stream():
        q_event = orjson.dumps(
            SseRes(
                id=q_msg.pk,
                content=data.content,
                type="HumanMessage",
            ).dict()
        )
        yield b"data: " + q_event + b"\n\n"
        a_message = await Message.objects.acreate(
            user_id=request.user.pk,
            role=Message.Role.AI,
            session_id=data.session_id,
        )
        a_message_content = ""
        async for chunk in model.astream([HumanMessage(content=data.content)]):
            if not chunk.content:
                continue
            a_message_content += str(chunk.content)
            event = orjson.dumps(
                SseRes(
                    id=a_message.pk,
                    content=str(chunk.content),
                    type=chunk.type,
                ).dict()
            )
            yield b"data: " + event + b"\n\n"
        a_message.body = {"content": a_message_content}
        await a_message.asave()

    response = StreamingHttpResponse(
        event_stream(),
        content_type="text/event-stream",
    )
    response["Cache-Control"] = "no-cache"
    return response
