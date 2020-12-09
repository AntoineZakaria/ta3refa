from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Person(models.Model,User):
    is_seller=models.BooleanField(default=False)
    Purchased_products=models.ArrayField(models.TextField())