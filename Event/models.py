from django.db import models
from django.conf import settings


class Event(models.Model):
    """This class represents Event model"""

    name = models.CharField(max_length=255, blank=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='events',
                              on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    alert_date = models.DateTimeField()
    alert_interval = models.DurationField()

    def __str__(self):
        return f"{self.name}"
