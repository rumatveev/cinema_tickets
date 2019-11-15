from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Movie


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows you to create new Movie and get all the Movies available.
    """
    queryset = Movie.objects.all().order_by('id')
    serializer_class = MovieSerializer