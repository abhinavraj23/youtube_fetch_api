from django.db import models

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
