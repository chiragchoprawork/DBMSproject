from django.shortcuts import render

from rest_framework import viewsets
from .models import Customer,AcdCustomer
from .serializers import CustomerSerializer,AcdCustomerSerializer

class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class AcdCustomerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AcdCustomer.objects.all()
    serializer_class = AcdCustomerSerializer

