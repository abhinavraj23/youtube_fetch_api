import os
# Cron Job
from django_cron import CronJobBase, Schedule

#Google API
from apiclient.discovery import build

from .models import *
from youtube_fetch_api import settings
from datetime import datetime, timedelta

class CallYoutubeApi(CronJobBase):
    RUN_EVERY_MINS = 10 #runs after every 10 minutes

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'api.call_youtube_api'    # a unique code
    time_now = datetime.now()
    last_request_time = time_now - timedelta(minutes=10)

    def do(self):
        apiKey = settings.GOOGLE_API_KEY
        youtube = build("youtube", "v3", developerKey= apiKey)

        # SOME BUG IS COMMING IN ISO FORMAT
        #req = youtube.search().list(q = "news", part = "snippet", order = "date", publishedAfter = self.last_request_time.isoformat())

        req = youtube.search().list(q = "cricket", part = "snippet", order = "date")
        res = req.execute()

        for item in res['items']:
            video_id = item['id']['videoId']
            publishedDateTime = item['snippet']['publishedAt']
            title = item['snippet']['title']
            description = item['snippet']['description']
            thumbnailsUrls = item['snippet']['thumbnails']['default']['url' ]
            channel_id = item['snippet']['channelId']
            channel_title = item['snippet']['channelTitle']
            print(title)
            Videos.objects.create(
                video_id = video_id,
                title = title,
                description = description,
                channel_id =channel_id,
                channel_title = channel_title,
                publishedDateTime = publishedDateTime,
                thumbnailsUrls = thumbnailsUrls,
            )

