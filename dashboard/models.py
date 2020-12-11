from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Shop(models.Model):
    shop_name = models.CharField(max_length=100)
    facebook_seller = models.CharField(max_length=100)
    gmail_seller = models.CharField(max_length=100)
    website_seller = models.CharField(max_length=100)
    mainshop_owner = models.IntegerField()
    phonenumber =models.CharField(max_length=100)
    admins= ArrayField(models.IntegerField())
    products= ArrayField(models.IntegerField())
    addrress =models.CharField(max_length=100)
    shop_money = models.FloatField()
    method_of_received_money = models.CharField(max_length=100)