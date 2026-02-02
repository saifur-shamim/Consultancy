from rest_framework import serializers
from .models import Appointment


class AppointmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ("consultant", "firm", "scheduled_at")

    def validate(self, data):
        conflict = Appointment.objects.filter(
            consultant=data["consultant"],
            scheduled_at=data["scheduled_at"],
            status__in=["PENDING", "CONFIRMED"],
        ).exists()

        if conflict:
            raise serializers.ValidationError(
                "Consultant is not available at this time."
            )

        return data

    def create(self, validated_data):
        user = self.context["request"].user
        return Appointment.objects.create(client=user, **validated_data)


class AppointmentListSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source="client.full_name", read_only=True)
    firm_name = serializers.CharField(source="firm.name", read_only=True)

    class Meta:
        model = Appointment
        fields = (
            "id",
            "client_name",
            "firm_name",
            "scheduled_at",
            "status",
            "created_at",
        )


class AppointmentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ("status",)

    def validate_status(self, value):
        allowed = ["CONFIRMED", "COMPLETED", "CANCELLED"]
        if value not in allowed:
            raise serializers.ValidationError("Invalid status update.")
        return value
