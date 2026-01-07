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


class SseRes(Schema):
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
    auth=None,
    response={200: SseRes, 400: ResponseSchema},
)
async def sse_stream(request: HttpRequest, data: SseReq):
    model = ChatOpenAI(
        model="gpt-5-nano",
        base_url=settings.CHAT_MODEL_BASE_URL,
        api_key=settings.CHAT_MODEL_API_KEY,
    )

    async def event_stream():
        async for chunk in model.astream([HumanMessage(content=data.content)]):
            event = orjson.dumps(
                SseRes(
                    content=str(chunk.content),
                    type=chunk.type,
                ).dict()
            )
            yield b"data: " + event + b"\n\n"

    response = StreamingHttpResponse(
        event_stream(),
        content_type="text/event-stream",
    )
    response["Cache-Control"] = "no-cache"
    return response
