from django.contrib.auth import get_user_model, password_validation
from rest_framework import serializers
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from src.base import exceptions as exc

from ..managers import CustomUserManager
from ..serializers import UserSerializer
from .tokens import get_tokens_for_user, get_user_for_unique_token
from .utils import get_user_by_email

User = get_user_model()


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)


class UserLogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(max_length=300, required=True)

    def save(self, **kwargs):
        try:
            RefreshToken(self.validated_data["refresh"]).blacklist()
        except TokenError:
            raise serializers.ValidationError("Token is invalid or expired")


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    A user serializer for registering the user
    """

    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "phone_number",
        )

    def validate_email(self, value):
        user = get_user_by_email(email=value)
        if user:
            if not user.is_active:
                raise exc.PermissionDenied(
                    "You have already registered, but did not verify your email. Please verify your email"
                )
            else:
                raise serializers.ValidationError("Email is already taken")
        return CustomUserManager.normalize_email(value)

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value


class ValidateRegisterSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)

    def validate_token(self, value):
        user = get_user_for_unique_token(value)
        if user.is_active:
            raise serializers.ValidationError("The user is already verified")
        return value


class EmptySerializer(serializers.Serializer):
    pass


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_current_password(self, value):
        if not self.context["request"].user.check_password(value):
            raise serializers.ValidationError("Current password does not match")
        return value

    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class VerificationLinkSerializer(PasswordResetSerializer):
    pass


class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)
    token = serializers.CharField(required=True)

    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value


class AuthUserSerializer(UserSerializer):
    tokens = serializers.SerializerMethodField()

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ("tokens",)

    def get_tokens(self, obj):
        return get_tokens_for_user(obj)
