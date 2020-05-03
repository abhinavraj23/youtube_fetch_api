from django.shortcuts import render
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializers import *
from .filter import CustomSearchFilter

# Rest FrameWork
from rest_framework import generics
from rest_framework.pagination import CursorPagination

from django.contrib.postgres.search import SearchQuery

class ResultsPagination(CursorPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100

# Searching is implemented using DRF Filters
# DRF filter by default uses [icontains] and thus the search by default supports partial searches

class YoutubeItems(generics.ListAPIView):
    filter_backends = (DjangoFilterBackend,filters.OrderingFilter)
    filterset_fields = ['channel_id','channel_title']
    ordering = ('-publishedDateTime')
    serializer_class = VideosSerializer
    pagination_class = ResultsPagination

    def get_queryset(self,view,request):
        qs = Videos.objects.all()
        search = request.GET.get("search", None)

        if search:
            try:
                search_string = self.request.GET['search']
                qs = qs.annotate(
                    search=(
                        SearchVector('title'))).filter(search__icontains=search_string)
            except KeyError:
                return Videos.objects.none()

        return qs.order_by('-publishedDateTime')

    # def get_queryset(self):
    #     search = self.request.GET.get("search", None)
    #     queryset = Videos.objects.all()

    #     if search:
    #         if '"' in search:
    #             query = SearchQuery(search.replace('"', ''), search_type='phrase')
    #         else:
    #             query = SearchQuery(search)
    #         queryset = queryset.filter(title_vector=query)
    #     else:
    #         queryset = queryset

    #     return queryset


