from django.http import HttpRequest
from ninja import Field, ModelSchema, Router, Schema

from domains.infra.django_ninja_utils import (
    JwtAuth,
    ListResponseSchema,
    ResponseSchema,
)
from domains.llm.models import Model

router = Router(auth=JwtAuth())


class CreateModelReq(Schema):
    name: str = Field()
    base_url: str = Field(
        default="",
    )
    api_key: str = Field(
        default="",
    )


class CreateModelRes(ModelSchema):
    class Meta:
        model = Model
        fields = "__all__"


class ListModelRes(ModelSchema):
    class Meta:
        model = Model
        fields = "__all__"


@router.post(
    "/model",
    summary="创建模型",
    response={200: ResponseSchema[CreateModelRes], 400: ResponseSchema},
)
def create_model(
    request: HttpRequest,
    data: CreateModelReq,
):
    model = Model.objects.create(
        name=data.name,
        base_url=data.base_url,
        api_key=data.api_key,
        user_id=request.user.pk,
    )
    return ResponseSchema(data=model)


@router.get(
    "/model",
    summary="获取模型列表",
    response={200: ListResponseSchema[ListModelRes], 400: ResponseSchema},
)
def list_models(
    request: HttpRequest,
    page: int = 1,
    size: int = 10,
):
    query = Model.objects.filter(user_id=request.user.pk)
    return ListResponseSchema.from_queryset(
        query,
        page,
        size,
    )
