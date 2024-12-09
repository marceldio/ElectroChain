from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import NetworkNodeViewSet, ProductAutocomplete
from . import views

router = DefaultRouter()
router.register(r'network', NetworkNodeViewSet, basename='network')

urlpatterns = router.urls

app_name = 'network'

urlpatterns = [
    path('product-autocomplete/', ProductAutocomplete.as_view(), name='product-autocomplete'),
    path('token/', obtain_auth_token, name='api_token_auth'),  # Эндпоинт для получения токена
] + router.urls

# urlpatterns = [
#     path('product-autocomplete/', views.ProductAutocomplete.as_view(), name='product-autocomplete'),
# ]
