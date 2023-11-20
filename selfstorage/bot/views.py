from django.http import JsonResponse
from django.core.serializers import serialize
from .models import Belongings, User, Storage
import json
# import logging
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt
from datetime import date, timedelta
# from django.shortcuts import get_object_or_404
# from django.views.decorators.http import require_http_methods


def bot_command(request):
    data_from_db = User.objects.all()
    serialized_data = serialize('json', data_from_db)
    return JsonResponse(serialized_data, safe=False)


def create_user(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        name = data.get('name')
        telegram_id = data.get('telegram_id')
        phonenumber = data.get('phonenumber')

        user, created = User.objects.get_or_create(
            telegram_id=telegram_id, defaults={
                'name': name, 'phonenumber': phonenumber})

        if created:
            return JsonResponse({
                "status": "success",
                "message":
                f"Пользователь {user.name} успешно зарегистрирован"})
        else:
            return JsonResponse(
                {"status": "error",
                 "message": "Пользователь уже зарегистрирован"})

    except Exception as e:
        return JsonResponse(
            {"status": e,
             "message": "Произошла ошибка при обработке запроса"})


@csrf_exempt
@require_POST
def my_belongings(request):
    try:
        data = json.loads(request.body)
        user_telegram_id = data.get('telegram_id')
        user = User.objects.get(telegram_id=user_telegram_id)

        if user.rented_box:
            belongings = Belongings.objects.filter(box=user.rented_box)
            serialized_data = [
                belonging.description for belonging in belongings]
            return JsonResponse(serialized_data, safe=False)
        else:
            return JsonResponse({'error': 'Вы не снимаете бокс'}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=400)


@csrf_exempt
@require_GET
def get_storage_address(request):
    storages = Storage.objects.all()
    storage_list = [storage.address for storage in storages]
    return JsonResponse(storage_list, safe=False)


@csrf_exempt
@require_POST
def check_registration(request):
    data = json.loads(request.body.decode('utf-8'))
    telegram_id = data.get('telegram_id')
    if telegram_id:
        try:
            registered = True
        except User.DoesNotExist:
            registered = False
    else:
        registered = False
    return JsonResponse({'registered': registered})


@csrf_exempt
def get_expiry_message(user, today):
    # data = json.loads(request.body.decode('utf-8'))
    # telegram_id = data.get('telegram_id')
    # today = date.today()
    # user = User.objects.get(telegram_id=telegram_id)
    one_month_from_today = today + timedelta(month=1)
    two_weeks_from_today = today + timedelta(days=14)
    one_week_from_today = today + timedelta(days=7)
    three_days_from_today = today + timedelta(days=3)

    if user.lease_end_date <= today:
        message = "Срок хранения ваших вещей закончился"
    elif user.lease_end_date <= three_days_from_today:
        message = "Срок хранения ваших вещей закончится через 3 дня"
    elif user.lease_end_date <= one_week_from_today:
        message = "Срок хранения ваших вещей закончится через 7 дней"
    elif user.lease_end_date <= two_weeks_from_today:
        message = "Срок хранения ваших вещей закончится через 2 недели"
    elif user.lease_end_date <= one_month_from_today:
        message = "Срок хранения ваших вещей закончится через 1 месяц"
    return message
