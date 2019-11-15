from django.test import TestCase
from tickets import models, factories


class TestModel(TestCase):
    def test_active_manager_works(self):
        factories.MovieFactory.create_batch(2, active=True)
        factories.MovieFactory(active=False)
        self.assertEqual(len(models.Movie.mv_objects.active()), 2)

    def test_can_create_showing(self):
        showing = factories.ShowingFactory()
        self.assertEqual(len(models.Movie.objects.all()), 1)

    def test_can_create_order(self):
        order = factories.OrderFactory()
        self.assertEqual(len(models.Order.objects.all()), 1)