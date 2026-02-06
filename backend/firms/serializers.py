from rest_framework import serializers
from .models import Firm


class FirmCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = ("name", "slug")

    def create(self, validated_data):
        return Firm.objects.create(owner=self.context["request"].user, **validated_data)
