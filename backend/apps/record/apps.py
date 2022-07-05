from django.apps import AppConfig
from django.db.models.signals import post_save, pre_save


class RecordConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.record'

    def ready(self) -> None:
        # from apps.record import tracking
        import apps.record.signals        