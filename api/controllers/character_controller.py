from django.http import JsonResponse
from api.services.character_service import CharacterService


def list_characters(request):
    data = CharacterService.list_characters()
    return JsonResponse(data, safe=False, status=200)
