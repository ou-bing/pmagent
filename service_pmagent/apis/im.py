import logging

from django.http import HttpRequest
from ninja import FilterSchema, ModelSchema, Query, Router

from domains.im.models import Message, Session
from domains.infra.django_ninja_utils import (
    JwtAuth,
    ListResponseSchema,
    ResponseSchema,
)

logger = logging.getLogger(__name__)

router = Router(auth=JwtAuth())


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
