from rest_framework import generics
from .models import Appointment
from .serializers import AppointmentCreateSerializer,  AppointmentListSerializer
from users.permissions import IsClient, IsConsultant


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
