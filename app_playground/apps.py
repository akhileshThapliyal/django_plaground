from django.apps import AppConfig
from iommi import register_style

from templates.styles.iommi_style import custom_style


class AppPlaygroundConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_playground'

    def ready(self):
        register_style('custom_style', custom_style)
