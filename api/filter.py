from rest_framework import filters

from .models import *
from .serializers import *

class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return super(CustomSearchFilter, self).get_search_fields(view, request)

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