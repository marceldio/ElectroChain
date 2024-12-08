from .models import NetworkNode, Contact, Product
from django.contrib import admin
from django.urls import reverse, path
from django.utils.html import format_html
from .forms import NetworkNodeAdminForm
from django.shortcuts import redirect
from django.contrib import messages


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house_number')
    search_fields = ('email', 'country', 'city')
    list_filter = ('country', 'city')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')
    search_fields = ('name', 'model')
    list_filter = ('release_date',)


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    form = NetworkNodeAdminForm
    list_display = ['name', 'supplier_link', 'contact', 'debt', 'created_at']
    search_fields = ['name', 'supplier__name', 'contact__email']
    ordering = ['created_at']
    list_filter = ('contact__country', 'contact__city',)  # Фильтр по стране, городу
    readonly_fields = ['supplier_link', 'clear_debt_button']  # Поля для ссылки на поставщика и действия
    actions = ['clear_debt']  # Вернем действие на страницу списка

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        # Добавляем динамическую фильтрацию для контактов
        if 'contact' in form.base_fields:
            form.base_fields['contact'].queryset = Contact.objects.all()

        return form

    def supplier_link(self, obj):
        """Кликабельная ссылка на страницу поставщика."""
        if obj.supplier:
            url = reverse('admin:network_networknode_change', args=[obj.supplier.id])
            return format_html('<a href="{}">{}</a>', url, obj.supplier.name)
        return "No Supplier"
    supplier_link.short_description = "Supplier"  # Название колонки

    def clear_debt_button(self, obj):
        """Кнопка для очистки задолженности на странице изменения."""
        if obj and obj.debt > 0:
            return format_html(
                '<a class="button" href="{}">Очистить задолженность</a>',
                reverse('admin:network_networknode_clear_debt', args=[obj.pk])
            )
        return "Нет задолженности"
    clear_debt_button.short_description = "Очистить задолженность"

    def get_urls(self):
        """Добавляем кастомный URL для кнопки очистки задолженности."""
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:pk>/clear-debt/',
                self.admin_site.admin_view(self.clear_debt_action),
                name='network_networknode_clear_debt',
            ),
        ]
        return custom_urls + urls

    def clear_debt_action(self, request, pk, *args, **kwargs):
        """Обработка действия очистки задолженности."""
        obj = self.get_object(request, pk)
        if obj:
            obj.debt = 0
            obj.save()
            self.message_user(request, "Задолженность успешно очищена.", messages.SUCCESS)
        return redirect('admin:network_networknode_change', obj.pk)

    @admin.action(description="Очистить задолженность перед поставщиком")
    def clear_debt(self, request, queryset):
        """Admin Action для очистки задолженности на странице списка."""
        queryset.update(debt=0)
        self.message_user(request, "Задолженность успешно очищена для выбранных объектов.")

    class Media:
        """Подключение пользовательских скриптов, если необходимо."""
        js = ('admin/js/clear_debt.js',)
