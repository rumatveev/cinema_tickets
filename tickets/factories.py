import factory
import factory.fuzzy
from . import models
import datetime
from datetime import timedelta


class MovieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Movie
        django_get_or_create = ('name',)

    name = factory.Sequence(lambda n: f'Group {n}')
    description = factory.Faker('text')


class ShowingRoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ShowingRoom

    capacity = factory.fuzzy.FuzzyInteger(10, 50)


class ShowingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Showing