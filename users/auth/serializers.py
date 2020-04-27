from django.contrib.auth import get_user_model, password_validation
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from ..managers import CustomUserManager
from ..serializers import UserSerializer
from .utils import get_user_by_email

User = get_user_model()


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    A user serializer for registering the user
    """

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
            raise serializers.ValidationError("Email is already taken")
        return CustomUserManager.normalize_email(value)

    def validate_password(self, value):
        password_validation.validate_password(value)
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


class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)
    token = serializers.CharField(required=True)

    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value

    def validate_token(self, value):
        try:
            Token.objects.get(key=value)
        except Token.DoesNotExist:
            raise serializers.ValidationError("Invalid token")
        return value


class AuthUserSerializer(UserSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ("auth_token",)

    def get_auth_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj)
        return token.key
