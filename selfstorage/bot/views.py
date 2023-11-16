from django.http import JsonResponse
from django.core.serializers import serialize
from .models import User


def bot_command(request):
    data_from_db = User.objects.all()
    serialized_data = serialize('json', data_from_db)
    return JsonResponse(serialized_data, safe=False)
