from django.db import models
from django.contrib.postgres.search import SearchVectorField, SearchVector

class Videos(models.Model):
    video_id = models.CharField(
        null=False,
        blank=False,
        max_length=200
    )

    title = models.CharField(
        null=True,
        blank=True,
        max_length=500
    )

    description = models.CharField(
        null=True,
        blank=True,
        max_length=5000
    )

    publishedDateTime = models.DateTimeField()

    thumbnailsUrls = models.URLField()

    channel_id = models.CharField(
        null=False,
        blank=False,
        max_length=500
    )

    channel_title = models.CharField(
        null=True,
        blank=True,
        max_length=500
    )

    created = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )

    title_vector = SearchVectorField(null=True)

    def make_search_vector(self):
        self.title_vector=SearchVector('title')

    def save(self, *args, **kwargs):
        self.make_search_vector()
        super(models.Model, self).save(*args, **kwargs)
