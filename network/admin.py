from django.contrib import admin
from .models import NetworkNode

@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city', 'supplier', 'debt', 'created_at')
    list_filter = ('country', 'city')
    search_fields = ('name', 'email', 'city', 'country')
    ordering = ('created_at',)

    # Действие для очистки задолженности
    actions = ['clear_debt']

    @admin.action(description="Очистить задолженность перед поставщиком")
    def clear_debt(self, request, queryset):
        queryset.update(debt=0)
        self.message_user(request, "Задолженность успешно очищена для выбранных объектов.")
