from django.shortcuts import render

from .models import *
from .serializers import *

#Rest FrameWork
from rest_framework import generics
from rest_framework.pagination import CursorPagination

class ResultsPagination(CursorPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class YoutubeItems(generics.ListAPIView):
    queryset = Videos.objects.all().order_by('-publishedDateTime')
    serializer_class = VideosSerializer
    pagination_class = ResultsPagination