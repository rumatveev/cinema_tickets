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

    capacity = factory.fuzzy.FuzzyInteger(10, 50)


class ShowingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Showing

    price_per_ticket = factory.fuzzy.FuzzyDecimal(10.0, 50.0)
    movie = factory.SubFactory(MovieFactory)
    showing_room = factory.SubFactory(ShowingRoomFactory)
    start = '2019-10-25 14:30'
    end = '2019-10-25 15:30'


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Order

    email = factory.Faker('email')
    showing = factory.SubFactory(ShowingFactory)
    quantity = factory.fuzzy.FuzzyInteger(1, 5)
