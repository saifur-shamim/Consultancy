from rest_framework import generics
from .serializers import AppointmentCreateSerializer
from users.permissions import IsClient


class AppointmentCreateView(generics.CreateAPIView):
    serializer_class = AppointmentCreateSerializer
    permission_classes = [IsClient]

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)
