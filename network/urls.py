from rest_framework.routers import DefaultRouter
from .views import NetworkNodeViewSet
from django.urls import path
from . import views

router = DefaultRouter()
router.register(r'network', NetworkNodeViewSet, basename='network')

urlpatterns = router.urls

app_name = 'network'

urlpatterns = [
    path('product-autocomplete/', views.ProductAutocomplete.as_view(), name='product-autocomplete'),
]
