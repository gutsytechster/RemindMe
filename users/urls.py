from rest_framework import routers

from users.auth.api import AuthViewSet
from users.api import UserViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('auth', AuthViewSet, basename='auth')
router.register('users', UserViewSet, basename='user')

urlpatterns = router.urls
