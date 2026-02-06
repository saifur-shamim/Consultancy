from rest_framework import serializers
from .models import ConsultantAvailability


class AvailabilityCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultantAvailability
        fields = ("start_time", "end_time")

    def validate(self, data):
        if data["start_time"] >= data["end_time"]:
            raise serializers.ValidationError("End time must be after start time.")
        return data

    def create(self, validated_data):
        user = self.context["request"].user
        return ConsultantAvailability.objects.create(consultant=user, **validated_data)


class AvailabilityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultantAvailability
        fields = (
            "id",
            "start_time",
            "end_time",
            "is_booked",
        )
