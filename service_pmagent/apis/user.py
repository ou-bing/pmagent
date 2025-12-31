from typing import Optional

from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpRequest
from jose import jwt
from ninja import Field, ModelSchema, Router, Schema

from domains.infra.django_ninja_utils import JwtAuth, ResponseSchema

router = Router()


class CreateTokenReq(Schema):
    username: str = Field()
    password: Optional[str] = Field(None)


class CreateTokenRes(Schema):
    accessToken: str = Field("", description="JWT")


class UserInfoRes(ModelSchema):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "is_staff"]


@router.post(
    "/token",
    response={200: ResponseSchema[CreateTokenRes], 400: ResponseSchema},
    auth=None,
    summary="",
)
def create_token(request: HttpRequest, data: CreateTokenReq):
    if data.password:
        user = authenticate(username=data.username, password=data.password)
        if user is None:
            return 400, ResponseSchema(code=1)
    payload = {"id": user.pk}
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

    return ResponseSchema(
        data=CreateTokenRes(
            accessToken=token,
        )
    )


@router.get(
    "/info",
    response={200: ResponseSchema[UserInfoRes]},
    auth=JwtAuth(),
    summary="获取当前用户信息",
)
def get_user_info(request: HttpRequest):
    return ResponseSchema(
        data=request.user,
    )
