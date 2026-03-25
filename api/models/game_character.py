from django.db import models


class GameCharacter(models.Model):
    game = models.ForeignKey(
        'Game',
        on_delete=models.CASCADE,
        db_column='game_id',
        related_name='game_characters',
        primary_key=True
    )
    character = models.ForeignKey(
        'Character',
        on_delete=models.CASCADE,
        db_column='character_id',
        related_name='game_characters'
    )

    class Meta:
        db_table = 'game_characters'
        managed = False
        unique_together = ('game', 'character')