from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from src.users.api import UserViewSet
from src.users.auth.api import AuthViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register("auth", AuthViewSet, basename="auth")
router.register("users", UserViewSet, basename="user")

urlpatterns = router.urls

urlpatterns += [path("auth/refresh", TokenRefreshView.as_view(), name="token_refresh")]
