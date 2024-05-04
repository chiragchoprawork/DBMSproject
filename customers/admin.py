from django.contrib import admin

# Register your models here.
# admin.py in your app
from .models import AcdCustomer

admin.site.register(AcdCustomer)

