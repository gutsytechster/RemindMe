from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from base.models import TimeStampedUUIDModel

from .managers import CustomUserManager


class CustomUser(AbstractUser, TimeStampedUUIDModel):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(
        _("First Name"), max_length=255, blank=True, null=False
    )
    last_name = models.CharField(_("Last Name"), max_length=255, blank=True, null=False)
    phone_number = PhoneNumberField(
        _("Phone Number"), max_length=15, blank=True, null=False, default=""
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email} - {self.first_name} {self.last_name}"
