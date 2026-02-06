from rest_framework import serializers
from .models import Appointment
from consultants.models import ConsultantAvailability


class AppointmentCreateSerializer(serializers.ModelSerializer):
    availability_id = serializers.PrimaryKeyRelatedField(
        queryset=ConsultantAvailability.objects.all(), source="availability"
    )

    class Meta:
        model = Appointment
        fields = ("availability_id", "firm")

    def validate_availability(self, availability):
        if availability.is_booked:
            raise serializers.ValidationError("Slot already booked.")
        return availability

class AppointmentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ["status"]

    def validate_status(self, value):
        allowed = ["CONFIRMED", "COMPLETED", "CANCELLED"]
        if value not in allowed:
            raise serializers.ValidationError("Invalid status")
        return value


class AppointmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
