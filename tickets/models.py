from django.db import models
from django.core.validators import MinValueValidator
from django.utils.text import slugify
import logging
import random
import string
from enum import Enum

logger = logging.getLogger(__name__)


def random_string(stringlength: int = 10) -> str:
    # Generate a random string of fixed length
    letters = string.ascii_lowercase
    return '_' + ''.join(random.choice(letters) for i in range(stringlength))


class ActiveManager(models.Manager):
    def active(self):
        return self.filter(active=True)


class ShowingRoom(models.Model):
    """
    This is a Showing Room model. Create one to accommodate customers and showings.
    """
    showing_room_name = models.CharField(max_length=32, unique=True, blank=False)
    capacity = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.showing_room_name


class Movie(models.Model):
    """
    If we need to add a new movie to the repertoire, we start here.
    """
    name = models.CharField(max_length=32, blank=False, unique=True)
    description = models.TextField(blank=True)
    date_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    objects = models.Manager()
    mv_objects = ActiveManager()


class Status(Enum):
    # helper class for Showing model status(choices) field
    ACTIVE = 10
    OUTDATED = 20  # for this I would rather run a celery task
    SOLD_OUT = 30


class Showing(models.Model):
    """
    This is our product would be: combination of a movie and a seat.
    """
    STATUSES = ((Status.ACTIVE.value, "Active"), (Status.OUTDATED.value, "Past"), (Status.SOLD_OUT.value, "Sold Out"))
    status = models.IntegerField(choices=STATUSES, default=Status.ACTIVE.value)

    name = models.CharField(max_length=100)
    price_per_ticket = models.DecimalField(max_digits=6, decimal_places=2)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    showing_room = models.ForeignKey(ShowingRoom, on_delete=models.DO_NOTHING)
    remaining_seats = models.PositiveIntegerField()
    start = models.DateTimeField()   # prefer standard '2019-10-25 14:30' date format
    end = models.DateTimeField()

    objects = models.Manager()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.remaining_seats is None:
            self.remaining_seats = self.showing_room.capacity
            # this is to create a 'unique' name for a showing
            self.name = slugify(self.movie.name + random_string())
            logger.info(f"Created new showing. Its name is {self.name}. Spasibo!")
        super(Showing, self).save(*args, **kwargs)


class Order(models.Model):
    """
    Paid Orders. I assume that the payment processing is not my headache in this challenge.
    """
    email = models.EmailField('email address')
    showing = models.ForeignKey(Showing, on_delete=models.PROTECT)
    # total of seats purchased
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    final_price = models.DecimalField(max_digits=6, decimal_places=2)

    def save(self, *args, **kwargs):
        self.final_price = self.showing.price_per_ticket * self.quantity
        logger.info(f'Successfully placed new order №{self.id} for {self.showing.name}')
        super(Order, self).save(*args, **kwargs)
