from django.contrib import admin
from .models import NetworkNode

@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city', 'supplier', 'debt', 'created_at')
    list_filter = ('country', 'city')
    search_fields = ('name', 'email', 'city', 'country')
    ordering = ('created_at',)

