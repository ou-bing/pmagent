from django.contrib.auth.models import User
from django.db import models


class Model(models.Model):
    name = models.CharField(max_length=255)
    base_url = models.CharField(
        max_length=255,
        blank=True,
        default="",
    )
    api_key = models.CharField(
        max_length=500,
        blank=True,
        default="",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
