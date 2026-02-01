from rest_framework import serializers
from .models import Firm


class FirmCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = ("name", "slug")

    def create(self, validated_data):
        user = self.context["request"].user
        return Firm.objects.create(owner=user, **validated_data)
