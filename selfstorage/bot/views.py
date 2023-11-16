# from django.shortcuts import render
from django.http import HttpResponse
from .models import User


def bot_command(request):
    data_from_db = User.objects.all()
    return HttpResponse(data_from_db)
