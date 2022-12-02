
from django.apps import AppConfig
from django.core.signals import request_started
from .tasks import log_request


class SymbolsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'symbols'

    def ready(self):
        request_started.connect(log_request)
