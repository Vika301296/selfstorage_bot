from django.urls import path
from .views import bot_command

urlpatterns = [
    path('bot_command/', bot_command, name='bot_command'),
]
