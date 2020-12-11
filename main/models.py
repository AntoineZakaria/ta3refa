from django.db import models

from django.contrib.postgres.fields import ArrayField
# Create your models here.
class comment :
    person_name=models.CharField(max_length=100)
    content = models.TextField()
    produc_id=models.CharField(max_length=100)

class Product(models.Model) :
    name = models.CharField(max_length=100)
    description = models.TextField() 
    price = models.FloatField()
    quantity = models.IntegerField()
    rate = models.IntegerField() 
    offer =  models.FloatField()
    comment=ArrayField(models.CharField(max_length=100),default=None)
    img =models.ImageField(upload_to= 'pics' )
    shop_id = models.CharField(max_length=100,default=None)








class Person(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    address=models.TextField(max_length=100)
    is_seller=models.BooleanField(default=False)
    Purchased_products=ArrayField(models.CharField(max_length=100))
