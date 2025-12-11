from typing import Optional

from django.conf import settings
from django.contrib.auth import authenticate
from django.http import HttpRequest
from jose import jwt
from ninja import Field, Router, Schema

from domains.infra.django_ninja_utils import ResponseSchema

router = Router()


class CreateTokenReq(Schema):
    username: str = Field()
    password: Optional[str] = Field(None)


class CreateTokenRes(Schema):
    id: int = Field()
    token: str = Field("", description="JWT")


@router.post(
    "/account/token",
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
            id=user.pk,
            token=token,
        )
    )
