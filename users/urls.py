from rest_framework import routers

from users.api import UserViewSet
from users.auth.api import AuthViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register("auth", AuthViewSet, basename="auth")
router.register("users", UserViewSet, basename="user")

urlpatterns = router.urls
