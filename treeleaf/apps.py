from django.apps import AppConfig


class TreeleafConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "treeleaf"

    def ready(self):
        import treeleaf.signals
