from rest_framework import serializers
from .models import Customer,AcdChecking, AcdCustomer, AcdHome, AcdInstitute, AcdInsurance, AcdLoan, AcdPersonal, AcdSafeAcnt, AcdSavings, AcdStudent, CustomersCustomer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id', 'customer_name']

class AcdCheckingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcdChecking
        fields = '__all__'


class AcdCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcdCustomer
        fields = '__all__'


class AcdHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcdHome
        fields = '__all__'


class AcdInstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcdInstitute
        fields = '__all__'


class AcdInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcdInsurance
        fields = '__all__'


class AcdLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcdLoan
        fields = '__all__'


class AcdPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcdPersonal
        fields = '__all__'


class AcdSafeAcntSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcdSafeAcnt
        fields = '__all__'


class AcdSavingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcdSavings
        fields = '__all__'


class AcdStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcdStudent
        fields = '__all__'


class CustomersCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomersCustomer
        fields = '__all__'
