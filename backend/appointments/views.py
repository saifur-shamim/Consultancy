from rest_framework import generics
from django.db import transaction
from rest_framework.exceptions import ValidationError

from .models import Appointment
from .serializers import (
    AppointmentCreateSerializer,
    AppointmentStatusSerializer,
    AppointmentListSerializer,
)
from consultants.models import ConsultantAvailability
from users.permissions import IsClient, IsConsultant


class BookAppointmentView(generics.CreateAPIView):
    serializer_class = AppointmentCreateSerializer
    permission_classes = [IsClient]

    @transaction.atomic
    def perform_create(self, serializer):
        availability = serializer.validated_data["availability"]
        availability = ConsultantAvailability.objects.select_for_update().get(
            id=availability.id
        )

        if availability.is_booked:
            raise ValidationError("Slot already booked")

        serializer.save(
            client=self.request.user,
            consultant=availability.consultant,
            scheduled_at=availability.start_time,
        )

        availability.is_booked = True
        availability.save()


class ConsultantAppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentListSerializer
    permission_classes = [IsConsultant]

    def get_queryset(self):
        return Appointment.objects.filter(consultant=self.request.user)


class AppointmentStatusUpdateView(generics.UpdateAPIView):
    serializer_class = AppointmentStatusSerializer
    permission_classes = [IsConsultant]

    def get_queryset(self):
        return Appointment.objects.filter(consultant=self.request.user)
