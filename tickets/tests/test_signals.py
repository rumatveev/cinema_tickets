from django.test import TestCase
from tickets import factories
from django.urls import reverse
from rest_framework import status
from tickets.models import Showing


class TestSignal(TestCase):

    def test_two_movies_one_place(self):
        # there should not be time overlaps: only one showing at one room at a time
        movie = factories.MovieFactory()
        room = factories.ShowingRoomFactory()
        showings = [{
            "price_per_ticket": "10",
            "movie": movie.id,
            "showing_room": room.id,
            "start": "2019-12-25 14:30",
            "end": "2019-12-25 15:30"
        },
        {
            "price_per_ticket": "10",
            "movie": movie.id,
            "showing_room": room.id,
            "start": "2019-12-25 14:00",
            "end": "2019-12-25 15:00"
        }]

        req_one = self.client.post(reverse("showings-list"), showings[0], format='json')
        self.assertEqual(req_one.status_code, status.HTTP_201_CREATED)
        req_two = self.client.post(reverse("showings-list"), showings[1], format='json')
        self.assertEqual(req_two.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Showing.objects.count(), 1)