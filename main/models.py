from django.db import models

from django.contrib.postgres.fields import ArrayField
# Create your models here.
class comment(models.Model) :
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
    img =models.ImageField(upload_to= 'product_image')
    shop_id = models.CharField(max_length=100,default=None)
    category = models.CharField(max_length=100,default=None)








class Person(models.Model):
    username=models.CharField(max_length=100)
    address=models.TextField(max_length=100)
    is_seller=models.BooleanField(default=False)
    Purchased_products=ArrayField(models.CharField(max_length=100))


class Seller(models.Model):
    username=models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100)
    telephone = models.IntegerField() 
    owned_products = ArrayField(models.CharField(max_length=100))

class Customer(models.Model):
    username=models.CharField(max_length=100)
    rated_products = ArrayField(models.CharField(max_length=100))
    commented_products = ArrayField(models.CharField(max_length=100))