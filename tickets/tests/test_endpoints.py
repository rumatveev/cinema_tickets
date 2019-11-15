from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from tickets import models, factories
import json


class TestEndpoints(APITestCase):
    def test_movie_flow(self):
        for i in range(10):
            factories.MovieFactory()

        response = self.client.get(reverse("movies-list"), follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_movie(self):
        data = {'name': 'Batman', 'description': 'Another Good Movie'}
        response = self.client.post(reverse("movies-list"), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Movie.objects.count(), 1)
        self.assertEqual(models.Movie.objects.get().name, 'Batman')

    def test_showing_rooms(self):
        room = {'showing_room_name': 'Argentina', 'capacity': '40'}
        response = self.client.post(reverse("rooms-list"), room, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.ShowingRoom.objects.count(), 1)
        self.assertEqual(models.ShowingRoom.objects.get().showing_room_name, 'Argentina')

        response = self.client.get(reverse("rooms-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

