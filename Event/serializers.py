from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.HyperlinkedModelSerializer):
    """This class serializes the Event model instance into formats like JSON"""
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail',
                                                read_only=True,)

    class Meta:
        model = Event
        fields = ('id', 'name', 'owner', 'creation_date',
                  'modified_date', 'alert_date', 'alert_interval',)
        read_only_fields = ('creation_date', 'modified_date',)
