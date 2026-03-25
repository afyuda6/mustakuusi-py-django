from django.db import models


class Character(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255)
    image_src = models.TextField(db_column="image_src")
    description = models.TextField(blank=True)
    position = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'characters'