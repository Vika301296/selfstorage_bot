from django.urls import path
from .views import bot_command, create_user

urlpatterns = [
    path('bot_command/', bot_command, name='bot_command'),
    path('create_user/', create_user, name='create_user'),
]
