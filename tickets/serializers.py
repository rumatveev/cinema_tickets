from rest_framework import serializers
from .models import Movie, ShowingRoom, Showing
from django.db.models import Q


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'description']


class ShowingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowingRoom
        fields = ['id', 'showing_room_name', 'capacity']


class ShowingSerializer(serializers.ModelSerializer):
    movie_name = serializers.ReadOnlyField(source='movie.name')
    remaining_seats = serializers.SerializerMethodField()

    class Meta:
        model = Showing
        fields = ['id', 'price_per_ticket', 'movie', 'movie_name', 'showing_room',  'remaining_seats', 'start', 'end']

    def get_remaining_seats(self, obj):
        #  this s.method returns remaining seats
        return obj.remaining_seats

    def validate(self, data):
        # need this to catch overlapping: we do not want to schedule
        # different showings at the same place and time
        if Showing.objects.filter(showing_room=data['showing_room']).filter(
                Q(start__gte=data['start'], start__lt=data['end']) |
                Q(end__gt=data['start'], end__lte=data['end'])).exists():
            raise serializers.ValidationError(f"This date and time is already booked at {data['showing_room']}!")
        if data['start'] == data['end']:
            raise serializers.ValidationError(f"Start and end should not be the same!")
        return data