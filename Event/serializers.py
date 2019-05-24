# from django.contrib.auth.models import User
from users.models import CustomUser
from rest_framework import serializers

from .models import Event


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """A user serializer to aid in authentication and authorization"""
    events = serializers.HyperlinkedRelatedField(many=True,
                                                 view_name='details',
                                                 read_only=True,)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'events')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    """This class serializes the Event model instance into formats like JSON"""
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail',
                                                read_only=True,)

    class Meta:
        model = Event
        fields = ('id', 'name', 'owner', 'creation_date',
                  'modified_date', 'alert_date', 'alert_interval',)
        read_only_fields = ('creation_date', 'modified_date',)
