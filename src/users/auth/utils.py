from uuid import UUID

from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from src.base import exceptions as exc

from ..email_content import PasswordReset


def get_and_authenticate_user(email, password):
    user = authenticate(username=email, password=password)
    if user is None:
        raise exc.BadRequest("Invalid username/password. Please try again!")
    return user


def create_user_account(email, password, first_name="", last_name="", **extra_fields):
    user = get_user_model().objects.create_user(
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
        **extra_fields
    )
    return user


def get_user_by_email(email: str):
    return get_user_model().objects.filter(email__iexact=email).first()


def send_password_reset_email(user, token):
    send_mail(
        subject=PasswordReset.subject,
        message=PasswordReset.body.format(name=user.first_name, token=token),
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=False,
    )


def encode_uuid_to_base64(uuid_) -> str:
    """Returns a  urlsafe based64 encoded representation of a UUID object or UUID like string.
    """
    return urlsafe_base64_encode(force_bytes(uuid_))


def decode_uuid_from_base64(uuid_value: str):
    """Given a base64 encoded string, try to decode it to a valid UUID object.
    Returns a valid UUID value or None
    """
    try:
        return UUID(force_text(urlsafe_base64_decode(uuid_value)))
    except (ValueError, OverflowError, TypeError):
        return None
