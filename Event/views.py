from rest_framework import generics
from rest_framework import permissions

from .permissions import IsOwnerOrReadOnly
from .serializers import EventSerializer
from .models import Event


class CreateView(generics.ListCreateAPIView):
    """This view performs POST http request to our api"""
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(owner=user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This view performs GET, PUT and DELETE http requests to our api"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly,)
