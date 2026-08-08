from django.contrib.auth.models import User
from rest_framework import serializers

from .enums import UserType
from .models import Run




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


class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'last_name', 'first_name')


class RunSerializer(serializers.ModelSerializer):
    athlete_data = AthleteSerializer(read_only=True, source='athlete')

    class Meta:
        model = Run
        fields = '__all__'

