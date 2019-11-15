from rest_framework import serializers
from .models import Movie, ShowingRoom


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'description']


class ShowingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowingRoom
        fields = ['id', 'showing_room_name', 'capacity']