from django.apps import AppConfig


class SysAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.sys_admin'

    def ready(self) -> None:
        # from apps.sys_admin import tracking
        import apps.record.signals