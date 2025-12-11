from typing import Any, Generic, List, Optional, TypeVar

import orjson
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import QuerySet
from jose import jwt
from ninja import Field, Schema
from ninja.pagination import AsyncPaginationBase
from ninja.renderers import BaseRenderer
from ninja.security import APIKeyHeader


class ORJSONRenderer(BaseRenderer):
    media_type = "application/json"

    def render(self, request, data, *, response_status):
        return orjson.dumps(data)


class JwtAuth(APIKeyHeader):
    param_name = "Authorization"

    def authenticate(self, request, key: str):
        try:
            payload = jwt.decode(
                key.replace("Bearer ", ""), settings.SECRET_KEY, algorithms=["HS256"]
            )
            user = User.objects.get(pk=payload["id"])
            return user
        except BaseException:
            return False


T = TypeVar("T")


class ResponseSchema(Schema, Generic[T]):
    code: int = 0
    message: str = ""
    data: Optional[T] = None


class PageInfo(Schema):
    total: int = 0
    current_page: int = 1
    last_page: int = 1


class ListData(Schema, Generic[T]):
    page_info: PageInfo = PageInfo()
    lists: List[T] = []


class ListResponseSchema(Schema, Generic[T]):
    code: int = 0
    message: str = ""
    data: ListData[T] = ListData()

    @classmethod
    def from_queryset(
        cls, items: QuerySet, page: int = 1, size: int = 10
    ) -> "ListResponseSchema[T]":
        offset = (page - 1) * size
        total = items.count()
        return ListResponseSchema[T](
            data=ListData[T](
                lists=list(items[offset : offset + size]),
                page_info=PageInfo(
                    total=total,
                    current_page=page,
                    last_page=(total + size - 1) // size,
                ),
            )
        )


class CustomPagination(AsyncPaginationBase):
    class Input(Schema):
        page: int = Field(1, ge=1)
        page_size: int = Field(10, ge=1)

    class Output(ResponseSchema):
        # data: List[Any] = []
        total: int = 0
        current_page: int = 1
        last_page: int = 1

    items_attribute = "data"

    def paginate_queryset(
        self,
        queryset: QuerySet,
        pagination: Input,
        **params: Any,
    ) -> Any:
        offset = (pagination.page - 1) * pagination.page_size
        total = self._items_count(queryset)
        result = {
            "data": queryset[offset : offset + pagination.page_size],
            "total": total,
            "current_page": pagination.page,
            "last_page": (total + pagination.page_size - 1) // pagination.page_size,
        }
        return result

    async def apaginate_queryset(
        self,
        queryset: QuerySet,
        pagination: Input,
        **params: Any,
    ) -> Any:
        offset = (pagination.page - 1) * pagination.page_size
        total = await self._aitems_count(queryset)
        return {
            "data": queryset[offset : offset + pagination.page_size],
            "total": total,
            "current_page": pagination.page,
            "last_page": (total + pagination.page_size - 1) // pagination.page_size,
        }
