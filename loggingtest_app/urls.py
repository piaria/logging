from django import views
from django.urls import path
from .views import get_tasks

urlpatterns = [
    path("tasks", get_tasks)
]