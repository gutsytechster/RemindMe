from django.conf import settings
from django.db import models

from src.base.models import TimeStampedUUIDModel


class Event(TimeStampedUUIDModel):
    """This class represents Event model"""

    name = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="events", on_delete=models.CASCADE
    )
    event_date = models.DateField()
    event_time = models.TimeField()
    has_reminder_sent = models.BooleanField(default=False)
    set_reminder = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"
