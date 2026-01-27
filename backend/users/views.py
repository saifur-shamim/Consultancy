from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .serializers import RegisterSerializer, ConsultantSerializer
from .permissions import IsClient


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class ConsultantListView(APIView):
    permission_classes = [IsClient]

    def get(self, request):
        consultants = User.objects.filter(role='CONSULTANT')
        serializer = ConsultantSerializer(consultants, many=True)
        return Response(serializer.data)
