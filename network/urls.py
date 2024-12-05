from rest_framework.routers import DefaultRouter
from .views import NetworkNodeViewSet
from django.urls import path


router = DefaultRouter()
router.register(r'network', NetworkNodeViewSet, basename='network')

urlpatterns = router.urls
