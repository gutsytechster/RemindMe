from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.HyperlinkedModelSerializer):
    """This class serializes the Event model instance into formats like JSON"""
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail',
                                                read_only=True,)

    class Meta:
        model = Event
        fields = ('url', 'id', 'name', 'owner', 'created_at',
                  'modified_at', 'alert_date', 'alert_interval',)
        read_only_fields = ('created_at', 'modified_at',)
