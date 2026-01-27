from rest_framework import serializers
from .models import Appointment


class AppointmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ["consultant", "firm", "scheduled_at"]
