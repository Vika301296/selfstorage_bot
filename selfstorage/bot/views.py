from django.http import JsonResponse
from django.core.serializers import serialize
from .models import User
import json
import logging
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt


def bot_command(request):
    data_from_db = User.objects.all()
    serialized_data = serialize('json', data_from_db)
    return JsonResponse(serialized_data, safe=False)

@csrf_exempt
@require_POST
def create_user(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        name = data.get('name')
        telegram_id = data.get('telegram_id')
        phonenumber = data.get('phonenumber')

        user, created = User.objects.get_or_create(telegram_id=telegram_id, defaults={'name': name, 'phonenumber': phonenumber})

        if created:
            return JsonResponse({"status": "success", "message": f"Пользователь {user.name} успешно зарегистрирован"})
        else:
            return JsonResponse({"status": "error", "message": "Пользователь уже зарегистрирован"})

    except Exception as e:
        return JsonResponse({"status": e, "message": "Произошла ошибка при обработке запроса"})


