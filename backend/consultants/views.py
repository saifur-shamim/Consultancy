from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import ConsultantAvailability
from .serializers import AvailabilityCreateSerializer, AvailabilityListSerializer
from users.permissions import IsConsultant


class CreateAvailabilityView(generics.CreateAPIView):
    serializer_class = AvailabilityCreateSerializer
    permission_classes = [IsConsultant]


class ConsultantAvailabilityListView(generics.ListAPIView):
    serializer_class = AvailabilityListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return ConsultantAvailability.objects.filter(
            consultant_id=self.kwargs["consultant_id"], is_booked=False
        ).order_by("start_time")
