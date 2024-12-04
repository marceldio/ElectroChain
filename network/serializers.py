from rest_framework import serializers
from .models import NetworkNode

class NetworkNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkNode
        exclude = ['debt']  # Поле "debt" исключено из API для обновления
