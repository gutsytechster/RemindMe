from rest_framework.routers import DefaultRouter

from .api import EventViewSet

default_router = DefaultRouter(trailing_slash=False)

default_router.register("events", EventViewSet, basename="event")

urlpatterns = default_router.urls
