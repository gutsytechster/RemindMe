from django.contrib.auth import get_user_model, logout
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated

from src.base import exceptions as exc
from src.base import response
from src.base.mixins import MultipleSerializerMixin

from ..serializers import UserSerializer
from . import serializers
from .tokens import (
    get_unique_token_for_user,
    get_user_for_unique_token,
    invalidate_all_tokens,
)
from .utils import (
    create_user_account,
    get_and_authenticate_user,
    get_user_by_email,
    send_password_reset_email,
    send_validate_registration_email,
)

User = get_user_model()


class AuthViewSet(MultipleSerializerMixin, viewsets.GenericViewSet):
    permission_classes = [
        AllowAny,
    ]
    serializer_class = serializers.EmptySerializer
    serializer_classes = {
        "login": serializers.UserLoginSerializer,
        "register": serializers.UserRegisterSerializer,
        "logout": serializers.UserLogoutSerializer,
        "validate_register": serializers.ValidateRegisterSerializer,
        "password_change": serializers.PasswordChangeSerializer,
        "password_reset": serializers.PasswordResetSerializer,
        "password_reset_confirm": serializers.PasswordResetConfirmSerializer,
        "send_verification_link": serializers.VerificationLinkSerializer,
    }

    @action(methods=["POST"], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_and_authenticate_user(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return response.Ok(data=data)

    @action(methods=["POST"], detail=False)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user_account(**serializer.validated_data)
        token = get_unique_token_for_user(user)
        send_validate_registration_email(user, token)
        data = UserSerializer(user).data
        return response.Created(data=data)

    @action(methods=["POST"], detail=False)
    def validate_register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_user_for_unique_token(serializer.validated_data["token"])
        user.is_active = True
        user.save()
        data = serializers.AuthUserSerializer(user).data
        return response.Ok(data=data)

    @action(methods=["POST"], detail=False)
    def send_verification_link(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_user_by_email(serializer.validated_data["email"])
        token = get_unique_token_for_user(user)
        send_validate_registration_email(user, token)
        return response.Ok()

    @action(methods=["POST"], detail=False, permission_classes=[IsAuthenticated])
    def logout(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logout(request)
        return response.NoContent()

    @action(methods=["POST"], detail=False, permission_classes=[IsAuthenticated])
    def password_change(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data["new_password"])
        request.user.save()
        return response.NoContent()

    @action(methods=["POST"], detail=False)
    def password_reset(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_user_by_email(serializer.validated_data["email"])
        if not user:
            raise exc.BadRequest("No user found with the given email")
        token = get_unique_token_for_user(user)
        send_password_reset_email(user, token)
        data = {
            "message": "Further instructions would be sent to the email if it exists"
        }
        return response.Ok(data=data)

    @action(methods=["POST"], detail=False)
    def password_reset_confirm(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_user_for_unique_token(serializer.validated_data["token"])
        user.set_password(serializer.validated_data["new_password"])
        user.save()
        invalidate_all_tokens(user)
        return response.NoContent()
