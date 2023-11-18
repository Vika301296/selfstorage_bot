from django.urls import path
from .views import bot_command, create_user, storage_address

urlpatterns = [
    path('bot_command/', bot_command, name='bot_command'),
    path('create_user/', create_user, name='create_user'),
    path('storage_address/', storage_address, name='storage_address')
]
