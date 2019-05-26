from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views

from .views import UserListView, UserDetailView, RegisterView

urlpatterns = [
    path('users/', UserListView.as_view(), name='list-user'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('api-auth-token/', views.obtain_auth_token, name='get_auth_token')
]

urlpatterns = format_suffix_patterns(urlpatterns)
