from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet,AcdCustomerViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'allcustomers',AcdCustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
