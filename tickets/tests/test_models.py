from django.test import TestCase
from tickets import models, factories


class TestModel(TestCase):
    def test_active_manager_works(self):
        factories.MovieFactory.create_batch(2, active=True)
        factories.MovieFactory(active=False)
        self.assertEqual(len(models.Movie.mv_objects.active()), 2)