from rest_framework import generics
from .models import Appointment
from .serializers import AppointmentCreateSerializer,  AppointmentListSerializer, AppointmentStatusSerializer
from users.permissions import IsClient, IsConsultant
from rest_framework.exceptions import PermissionDenied

class BookAppointmentView(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentCreateSerializer
    permission_classes = [IsClient]


class MyAppointmentsView(generics.ListAPIView):
    """
    Consultant views his own appointments
    """

    serializer_class = AppointmentListSerializer
    permission_classes = [IsConsultant]

    def get_queryset(self):
        user = self.request.user
        return Appointment.objects.filter(consultant=user).order_by("scheduled_at")


class AppointmentStatusUpdateView(generics.UpdateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentStatusSerializer
    permission_classes = [IsConsultant]

    def get_object(self):
        appointment = super().get_object()
        if appointment.consultant != self.request.user:
            raise PermissionDenied("Not your appointment")
        return appointment