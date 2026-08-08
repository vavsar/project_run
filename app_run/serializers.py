from django.contrib.auth.models import User
from rest_framework import serializers

from .enums import UserType
from .models import Run

class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Run
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'date_joined', 'username', 'last_name', 'first_name', 'type')

    def get_type(self, obj):
        if obj.is_staff:
            user_type = UserType.COACH
        else:
            user_type = UserType.ATHLETE

        return user_type

