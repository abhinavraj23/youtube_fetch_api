from django.shortcuts import render
from rest_framework import filters

from .models import *
from .serializers import *

# Rest FrameWork
from rest_framework import generics
from rest_framework.pagination import CursorPagination

class ResultsPagination(CursorPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# Searching is implemented using DRF Filters
# DRF filter by default uses [icontains] and thus the search by default supports partial searches

class YoutubeItems(generics.ListAPIView):
    search_fields = ['title', 'description']
    filter_backends = (filters.SearchFilter,)
    queryset = Videos.objects.all().order_by('-publishedDateTime')
    serializer_class = VideosSerializer
    pagination_class = ResultsPagination
