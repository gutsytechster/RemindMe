from django.db import models
from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver


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


# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL,
#                                 on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=255, blank=False)
#     last_name = models.CharField(max_length=255, blank=False)
#     phone_number = models.CharField(max_length=15, blank=False)


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
