from api.models import Game
from django.db.models import Prefetch
from api.models import GameCharacter, Screenshot


class GameRepository:

    @staticmethod
    def get_all_with_relations():
        return (
            Game.objects
            .prefetch_related(
                'screenshots',
                Prefetch(
                    'game_characters',
                    queryset=GameCharacter.objects.select_related('character')
                )
            )
            .order_by('-release_date', '-id')
        )
