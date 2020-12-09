from django.db import models

from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Person(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    address=models.TextField(max_length=100)
    is_seller=models.BooleanField(default=False)
    Purchased_products=ArrayField(models.CharField(max_length=100))