from django.contrib.auth import get_user_model, logout
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from src.base.mixins import MultipleSerializerMixin

from . import serializers
from .tokens import (
    get_token_for_password_reset,
    get_user_for_password_reset_token,
    invalidate_all_tokens,
)
from .utils import (
    create_user_account,
    get_and_authenticate_user,
    get_user_by_email,
    send_password_reset_email,
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
        "password_change": serializers.PasswordChangeSerializer,
        "password_reset": serializers.PasswordResetSerializer,
        "password_reset_confirm": serializers.PasswordResetConfirmSerializer,
    }

    @action(methods=["POST"], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_and_authenticate_user(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=["POST"], detail=False)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user_account(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_201_CREATED)

    @action(methods=["POST"], detail=False, permission_classes=[IsAuthenticated])
    def logout(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=["POST"], detail=False, permission_classes=[IsAuthenticated])
    def password_change(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data["new_password"])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=["POST"], detail=False)
    def password_reset(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_user_by_email(serializer.validated_data["email"])
        if user:
            token = get_token_for_password_reset(user)
            send_password_reset_email(user, token)
        data = {
            "message": "Further instructions would be sent to the email if it exists"
        }
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=["POST"], detail=False)
    def password_reset_confirm(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_user_for_password_reset_token(serializer.validated_data["token"])
        user.set_password(serializer.validated_data["new_password"])
        user.save()
        invalidate_all_tokens(user)
        return Response(status=status.HTTP_204_NO_CONTENT)
