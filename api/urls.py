from django.urls import path
from api.controllers.character_controller import list_characters
from api.controllers.game_controller import list_games

urlpatterns = [
    path('characters/', list_characters),
    path('games/', list_games),
]
