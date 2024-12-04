from django.db import models

class NetworkNode(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    email = models.EmailField(verbose_name="Email")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    house_number = models.CharField(max_length=10, verbose_name="Номер дома")
    product_name = models.CharField(max_length=255, verbose_name="Название продукта")
    product_model = models.CharField(max_length=100, verbose_name="Модель продукта")
    product_release_date = models.DateField(verbose_name="Дата выхода продукта")
    supplier = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL, related_name="clients", verbose_name="Поставщик"
    )
    debt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Задолженность перед поставщиком")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return self.name
