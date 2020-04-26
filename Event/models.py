from django.db import models
from django.conf import settings

from base.models import TimeStampedUUIDModel


class Event(TimeStampedUUIDModel):
    """This class represents Event model"""

    name = models.CharField(max_length=255, blank=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='events',
                              on_delete=models.CASCADE)
    alert_date = models.DateTimeField()
    alert_interval = models.DurationField()

    def __str__(self):
        return f"{self.name}"
