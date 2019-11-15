from rest_framework import viewsets
from .serializers import MovieSerializer, ShowingRoomSerializer
from .models import Movie, ShowingRoom


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows you to create new Movie and get all the Movies available.
    """
    queryset = Movie.objects.all().order_by('id')
    serializer_class = MovieSerializer


class ShowingRoomViewSet(viewsets.ModelViewSet):
    """
    This is for the access to the Rooms: create one or get list of existing
    """
    queryset = ShowingRoom.objects.all().order_by('id')
    serializer_class = ShowingRoomSerializer