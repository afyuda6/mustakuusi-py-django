from django.db import models


class Screenshot(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    game = models.ForeignKey(
        'Game',
        on_delete=models.CASCADE,
        db_column='game_id',
        related_name='screenshots'
    )
    image_src = models.TextField(db_column='image_src')

    def __str__(self):
        return f"Screenshot {self.id}"

    class Meta:
        db_table = 'screenshots'
