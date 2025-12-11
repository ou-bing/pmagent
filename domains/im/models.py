from django.contrib.auth.models import User
from django.db import models


class Session(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    title = models.CharField(
        default="",
        max_length=255,
        blank=True,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ["-id"]

    def __str__(self) -> str:
        return f"{self.pk} - {self.title}"


class Message(models.Model):
    class Role(models.TextChoices):
        HUMAN = "human", "human"
        AI = "ai", "ai"
        SYSTEM = "system", "system"
        TOOL = "tool", "tool"

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    cost = models.BigIntegerField(
        default=0,
    )
    body = models.JSONField(
        default=dict,
    )
    sequence = models.PositiveIntegerField(
        default=0,
    )
    role = models.CharField(max_length=32, choices=Role.choices)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    session = models.ForeignKey(
        Session,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ["-id"]

    def __str__(self) -> str:
        return f"{self.session.pk} - {self.pk}"
