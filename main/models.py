from django.db import models

# Create your models here.
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








