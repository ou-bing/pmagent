from django.apps import AppConfig


class ServicePmagentConfig(AppConfig):
    name = "service_pmagent"

    def ready(self):
        from service_pmagent.interfaces.admin import im  # noqa
