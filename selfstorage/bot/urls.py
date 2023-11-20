from django.urls import path
from .views import bot_command, check_registration
from .views import create_user, my_belongings, get_storage_address


urlpatterns = [
    path('bot_command/', bot_command, name='bot_command'),
    path('create_user/', create_user, name='create_user'),
    path('storage_address/', get_storage_address, name='storage_address'),
    path('my_belongings/', my_belongings, name='my_belongings'),
    path('check_registration/', check_registration, name='check_registration')
]
