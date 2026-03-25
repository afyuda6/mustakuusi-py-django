from django.http import JsonResponse
from api.services.game_service import GameService


def list_games(request):
    data = GameService.list_games()
    return JsonResponse(data, safe=False, status=200)
