from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)

    def __str__(self):
        return self.customer_name
