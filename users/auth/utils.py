from django.contrib.auth import authenticate, get_user_model
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import serializers

from ..email_content import PasswordReset


def get_and_authenticate_user(email, password):
    user = authenticate(username=email, password=password)
    if user is None:
        raise serializers.ValidationError("Invalid username/password. Please try again!")
    return user


def create_user_account(email, password, first_name="",
                        last_name="", **extra_fields):
    user = get_user_model().objects.create_user(
        email=email, password=password, first_name=first_name,
        last_name=last_name, **extra_fields)
    return user


def get_user_by_email(email: str):
    return get_user_model().objects.filter(email__iexact=email).first()


def send_password_reset_email(user, token):
    send_mail(
        subject=PasswordReset.subject,
        message=PasswordReset.body.format(name=user.first_name, token=token),
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=False
    )
