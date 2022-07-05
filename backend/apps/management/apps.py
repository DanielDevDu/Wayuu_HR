from django.apps import AppConfig


class ManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.management'

    def ready(self):
        # from apps.management import tracking
        from apps.management import signals