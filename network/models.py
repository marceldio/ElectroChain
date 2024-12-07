from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Contact(models.Model):
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.email}, {self.city}, {self.street}, {self.house_number}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return self.name


class NetworkNode(models.Model):
    name = models.CharField(max_length=100, unique=True)
    contact = models.OneToOneField(
        'Contact',
        on_delete=models.CASCADE,
    )
    products = models.ManyToManyField(
        'Product',
        related_name='network_nodes',
    )
    supplier = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='supplied_network_nodes',
    )
    debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00  # значение по умолчанию
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Обычное сохранение данных

# Сигнал для проверки продуктов после сохранения объекта
@receiver(post_save, sender=NetworkNode)
def filter_products_after_save(sender, instance, **kwargs):
    if instance.supplier:  # Если указан поставщик
        supplier_products = Product.objects.filter(network_nodes=instance.supplier)
        invalid_products = instance.products.exclude(id__in=supplier_products)
        if invalid_products.exists():
            instance.products.remove(*invalid_products)