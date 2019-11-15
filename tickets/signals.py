import logging
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Order, Showing
from datetime import timedelta
from django.utils import timezone

logger = logging.getLogger(__name__)

# this is not very elegant, but still rather effective way to remove seats from the
# corresponding showing and change status to sold out if needed
@receiver(pre_save, sender=Order)
def remove_seats_from_showing(sender, instance, **kwargs):
    logger.info(f"Creating new order for {instance.email}\nRemoving seats from {instance.showing.name}")

    showing_obj = Showing.objects.get(id=instance.showing.id)
    showing_obj.remaining_seats = showing_obj.remaining_seats - instance.quantity
    if showing_obj.remaining_seats == 0:
        showing_obj.status = 30
        logger.info(f'We have a sold out here!')

    logger.info(f"Now {showing_obj.name} has only {showing_obj.remaining_seats} seats")

    showing_obj.save()


# I do not particularly like this solution - it is rather for a proof of concept.
@receiver(pre_save, sender=Showing)
def mark_outdated_showings(sender, **kwargs):
    logger.info(f"Removing outdated showings")
    threshold = timezone.now() - timedelta(days=1)
    Showing.objects.filter(start__lte=threshold).update(status=20)