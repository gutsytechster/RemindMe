from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework_simplejwt.tokens import RefreshToken

from src.base import exceptions as exc

from .utils import decode_uuid_from_base64, encode_uuid_to_base64


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


def get_unique_token_for_user(user):
    return "{}::{}".format(
        encode_uuid_to_base64(user.pk), PasswordResetTokenGenerator().make_token(user)
    )


def get_user_for_unique_token(token):
    default_error_messages = {
        "invalid_token": "Invalid token or the token has expired",
        "user_not_found": "No user exists for given token",
    }
    try:
        uidb64, reset_token = token.split("::")
    except ValueError:
        raise exc.RequestValidationError(default_error_messages["invalid_token"])

    user_id = decode_uuid_from_base64(uidb64)
    if not user_id:
        raise exc.RequestValidationError(default_error_messages["invalid_token"])

    user = get_user_model().objects.filter(id=user_id).first()

    if not user:
        raise exc.RequestValidationError(default_error_messages["user_not_found"])

    if not PasswordResetTokenGenerator().check_token(user, reset_token):
        raise exc.RequestValidationError(default_error_messages["invalid_token"])

    return user


def invalidate_all_tokens(user):
    tokens = OutstandingToken.objects.filter(user=user)
    for token in tokens:
        try:
            RefreshToken(token.token).blacklist()
        except TokenError:
            # If raised, don't interrupt the process
            pass
