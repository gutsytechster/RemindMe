from django.contrib.auth import get_user_model, logout
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from . import serializers
from .utils import get_and_authenticate_user, create_user_account, get_user_by_email, send_password_reset_email
from base.mixins import MultipleSerializerMixin

User = get_user_model()


class AuthViewSet(MultipleSerializerMixin, viewsets.GenericViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = serializers.EmptySerializer
    serializer_classes = {
        'login': serializers.UserLoginSerializer,
        'register': serializers.UserRegisterSerializer,
        'logout': serializers.EmptySerializer,
        'password_change': serializers.PasswordChangeSerializer,
        'password_reset': serializers.PasswordResetSerializer,
        'password_reset_confirm': serializers.PasswordResetConfirmSerializer,
    }

    @action(methods=['POST', ], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_and_authenticate_user(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST', ], detail=False)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user_account(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_201_CREATED)

    @action(methods=['POST'], detail=False, permission_classes=[IsAuthenticated, ])
    def logout(self, request):
        logout(request)
        request.auth.delete()
        data = {'success': 'Sucessfully logged out'}
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=False, permission_classes=[IsAuthenticated, ])
    def password_change(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['POST'], detail=False)
    def password_reset(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_user_by_email(serializer.validated_data['email'])
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            send_password_reset_email(user, token.key)
        data = {'message': 'Further instructions would be sent to the email if it exists'}
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=False)
    def password_reset_confirm(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data["token"]
        token = Token.objects.get(key=token)
        token.user.set_password(serializer.validated_data["new_password"])
        token.user.save()
        token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
