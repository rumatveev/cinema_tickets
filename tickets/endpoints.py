from rest_framework import viewsets
from .serializers import (MovieSerializer, ShowingRoomSerializer, ShowingSerializer, OrderSerializer)
from .models import (Movie, ShowingRoom, Showing, Order)


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


class ShowingViewSet(viewsets.ModelViewSet):
    """
    This endpoint will return those showings which are not sold out and relevant
    """
    queryset = Showing.objects.filter(status=10).order_by('id')
    serializer_class = ShowingSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    Here we can create new orders and get the list of the past orders
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer