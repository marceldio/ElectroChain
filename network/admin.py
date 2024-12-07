from django.contrib import admin
from .models import NetworkNode, Contact, Product
from .forms import NetworkNodeAdminForm


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
    list_display = ['name', 'supplier', 'contact', 'debt', 'created_at']
    search_fields = ['name', 'supplier__name', 'contact__email']
    ordering = ['created_at']

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "products":
            supplier_id = request.GET.get('supplier')
            if supplier_id:  # Если поставщик выбран
                kwargs["queryset"] = Product.objects.filter(network_nodes=supplier_id)
            else:  # Если поставщик не выбран, показываем все продукты
                kwargs["queryset"] = Product.objects.all()
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    # Действие для очистки задолженности
    actions = ['clear_debt']

    @admin.action(description="Очистить задолженность перед поставщиком")
    def clear_debt(self, request, queryset):
        queryset.update(debt=0)
        self.message_user(request, "Задолженность успешно очищена для выбранных объектов.")

    def get_supplier(self, obj):
        return obj.supplier.name if obj.supplier else 'Нет поставщика'
    get_supplier.short_description = 'Поставщик'

    def get_country(self, obj):
        return obj.contact.country if obj.contact else 'Нет данных'
    get_country.short_description = 'Страна'

    def get_city(self, obj):
        return obj.contact.city if obj.contact else 'Нет данных'
    get_city.short_description = 'Город'
