"""Core API URL Configuration"""
from django.urls import path
from . import views

APP_NAME = 'core_api'
urlpatterns = [
    path('test/', views.test, name='test')
]
