from rest_framework import mixins, viewsets
from rest_framework import permissions

from .permissions import IsOwnerOrReadOnly
from .serializers import EventSerializer
from .models import Event


class EventViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin, mixins.CreateModelMixin,
                   mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Event.objects.filter(owner=self.request.user)
