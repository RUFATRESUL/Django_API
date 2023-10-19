from django_filters import rest_framework as filters
from .models import Movie

class MovieFilter(filters.FilterSet):
    max_date = filters.DateFilter('released', lookup_expr='lte')
    min_date = filters.DateFilter('released', lookup_expr='gte')

    class Meta:
        model = Movie
        fields = ['genres','director']