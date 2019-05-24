from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView, UserListView, UserDetailView

urlpatterns = [
    path('events/', CreateView.as_view(), name='create'),
    path('events/<int:pk>/', DetailsView.as_view(), name='details'),
    path('users/', UserListView.as_view(), name='list-user'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
