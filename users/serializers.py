from django.contrib.auth import get_user_model, password_validation
# from django.core import exceptions

from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """A user serializer to aid in authentication and authorization"""
    events = serializers.HyperlinkedRelatedField(many=True,
                                                 view_name='details',
                                                 read_only=True,)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'phone_number',
                  'events')


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    A user serializer for registering the user
    """
    password = serializers.CharField(write_only=True)

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value

    def create(self, request):
        user = User.objects.create(**self.validated_data)
        user.set_password(request.get('password'))
        user.save()
        return user

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name',
                  'phone_number',)
