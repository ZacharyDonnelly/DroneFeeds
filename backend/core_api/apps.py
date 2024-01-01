"""Core API app config"""
from django.apps import AppConfig


class CoreAPIConfig(AppConfig):
    """core API app config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_api'
