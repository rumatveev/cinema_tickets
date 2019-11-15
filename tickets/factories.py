import factory
import factory.fuzzy
from . import models


class MovieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Movie
        django_get_or_create = ('name',)

    name = factory.Sequence(lambda n: f'Group {n}')
    description = factory.Faker('text')


class ShowingRoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ShowingRoom

    showing_room_name = factory.Iterator(["Argentina", "Canada", "France", "Italy", "Spain"])
    capacity = factory.fuzzy.FuzzyInteger(10, 50)