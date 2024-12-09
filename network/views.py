from rest_framework import viewsets
from .models import NetworkNode
from .serializers import NetworkNodeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from dal import autocomplete
from .models import Product


class ProductAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Если пользователь не аутентифицирован, возвращаем пустой набор
        if not self.request.user.is_authenticated:
            return Product.objects.none()

        # Получаем фильтр по поставщику, если он указан
        supplier_id = self.forwarded.get('supplier', None)
        if supplier_id:
            return Product.objects.filter(network_nodes=supplier_id)
        return Product.objects.all()


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
