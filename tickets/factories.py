import factory
import factory.fuzzy
from . import models


class MovieFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: f'Group {n}')
    description = factory.Faker('text')

    class Meta:
        model = models.Movie
        django_get_or_create = ('name',)