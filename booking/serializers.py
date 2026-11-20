from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Booking

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'id',
            'user',
            'event_id',
            'room_number',
            'start_time',
            'end_time'
        ]
        read_only_fields = ['user', 'event_id']