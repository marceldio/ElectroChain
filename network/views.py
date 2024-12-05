from rest_framework import viewsets
from .models import NetworkNode
from .serializers import NetworkNodeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class NetworkNodeViewSet(viewsets.ModelViewSet):
    """
    CRUD для модели NetworkNode.
    Поле 'debt' доступно только для чтения.
    """
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

