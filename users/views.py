from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from .serializers import UserSerializer, UserRegisterSerializer

User = get_user_model()


class UserListView(generics.ListAPIView):
    """This view lists all the users in the database"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    """This view retrieves the information of the user"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    model = User
    permission_classes = (permissions.AllowAny,)
