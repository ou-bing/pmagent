"""
URL configuration for pmagent project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import logging

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path, re_path
from ninja import NinjaAPI

from domains.infra.django_ninja_utils import ORJSONRenderer
from service_pmagent.apis.im import router as im_router
from service_pmagent.apis.user import router as user_router
from service_pmagent.wss import chat

logger = logging.getLogger(__name__)


api = NinjaAPI(
    renderer=ORJSONRenderer(),
    docs_decorator=staff_member_required,
    version="mobile",
)


@api.exception_handler(Exception)
def service_unavailable_api(request, exc: Exception):
    logger.exception("Service unavailable")
    return api.create_response(
        request,
        {"code": 1, "message": f"{exc}"},
        status=500,
    )


api.add_router("user", user_router, tags=["user"])
api.add_router("im", im_router, tags=["im"])


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<session_id>\w+)/$", chat.AsyncChatConsumer.as_asgi()),  # type: ignore
]
