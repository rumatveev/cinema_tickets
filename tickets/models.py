from django.db import models


class ActiveManager(models.Manager):
    def active(self):
        return self.filter(active=True)


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
