from django.shortcuts import render
from rest_framework.response import Response  # Import Response class
from rest_framework import viewsets
from .models import Customer,AcdCustomer
from .serializers import CustomerSerializer,AcdCustomerSerializer

class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class AcdCustomerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AcdCustomer.objects.all()
    serializer_class = AcdCustomerSerializer

    def list(self, request, *args, **kwargs):
        queryset = AcdCustomer.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        print("this is count  ",queryset)
        print("Serialized data:", serializer.data)  # Print serialized data
        return Response(serializer.data) 

