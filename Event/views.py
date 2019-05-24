# from django.contrib.auth.models import User
from users.models import CustomUser
from rest_framework import generics

from .serializers import EventSerializer, UserSerializer
from .models import Event


class CreateView(generics.ListCreateAPIView):
    """This view performs POST http request to our api"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This view performs GET, PUT and DELETE http requests to our api"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class UserListView(generics.ListAPIView):
    """This view lists all the users in the database"""
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    """This view retrieves the information of the user"""
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
