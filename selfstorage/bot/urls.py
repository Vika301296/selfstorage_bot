from django.urls import path
from .views import bot_command, create_user, check_registration

urlpatterns = [
    path('bot_command/', bot_command, name='bot_command'),
    path('create_user/', create_user, name='create_user'),
    path('check_registration/', check_registration, name='check_registration')
]
