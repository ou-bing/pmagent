from django.contrib import admin

from domains.im.models import Message, Session


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass
