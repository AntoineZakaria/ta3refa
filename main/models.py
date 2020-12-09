from django.db import models

from django.contrib.postgres.fields import ArrayField
# Create your models here.
<<<<<<< HEAD
class comment :
    pass

class Product(models.Model) :
    name = models.CharField(max_length=100)
    discrriptio = models.TextField() 
    price = models.FloatField()
    quantity = models.IntegerField()
    rate = models.IntegerField() 
    offer =  models.FloatField()
    comments :comment
    img =models.ImageField(upload_to= 'pics' )








=======
class Person(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    address=models.TextField(max_length=100)
    is_seller=models.BooleanField(default=False)
    Purchased_products=ArrayField(models.CharField(max_length=100))
>>>>>>> 132595db565c9e7def59c3ef5a26c1463e60aac8
