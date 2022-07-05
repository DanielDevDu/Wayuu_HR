from django.apps import AppConfig


class LegalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.legal'

    # def ready(self) -> None:
        # from apps.legal import tracking