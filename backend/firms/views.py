from rest_framework import generics
from .models import Firm
from .serializers import FirmCreateSerializer
from .permissions import IsFirmOwner


class FirmCreateView(generics.CreateAPIView):
    serializer_class = FirmCreateSerializer
    permission_classes = [IsFirmOwner]
