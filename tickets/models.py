from django.db import models
from django.core.validators import MinValueValidator


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
