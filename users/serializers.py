from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'phone_number',
                  'is_staff', 'is_active')
        read_only_fields = ('id', 'email', 'is_staff', 'is_active')
