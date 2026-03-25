from django.db import models


class Game(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    title = models.CharField(max_length=255)
    image_src = models.TextField()
    release_date = models.DateTimeField()
    description = models.TextField()
    categories_raw = models.TextField(db_column="categories", blank=True)
    detail = models.TextField(blank=True)
    privacy_policy_link = models.TextField(blank=True)
    download_link = models.TextField(blank=True)
    long_description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    @property
    def categories(self):
        if not self.categories_raw:
            return []

        trimmed = self.categories_raw.strip("{}")
        parts = trimmed.split(",")

        return [p.strip('"') for p in parts]

    class Meta:
        db_table = 'games'
