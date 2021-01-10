from django.db import models

from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Comment(models.Model) :
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
    #comment=ArrayField(models.CharField(max_length=100),default=None)
    comment = ArrayField(ArrayField(models.CharField(max_length=100,blank=True),size=3),size=100,default=None)
    img =models.ImageField(upload_to= 'product_image')
    shop_id = models.CharField(max_length=100,default=None)
    category = models.CharField(max_length=100,default=None)
    def new_price (self):
        new_price=(self.price)-(self.price)*(self.offer)*0.01
        return new_price









class Person(models.Model):
    username=models.CharField(max_length=100)
    address=models.TextField(max_length=100)
    is_seller=models.BooleanField(default=False)
    Purchased_products=ArrayField(models.CharField(max_length=100))
    favourite_products=ArrayField(models.CharField(max_length=100))


class Seller(models.Model):
    username=models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100)
    telephone = models.IntegerField() 
    owned_products = ArrayField(models.CharField(max_length=100))
    current_balance = models.IntegerField()

class Customer(models.Model):
    username=models.CharField(max_length=100)
    rated_products = ArrayField(models.CharField(max_length=100))
    commented_products = ArrayField(models.CharField(max_length=100))

class mail_verification(models.Model):
    user_name= models.TextField() 
    message_code=models.TextField() 
    is_autonticated=models.BooleanField(default=False)
