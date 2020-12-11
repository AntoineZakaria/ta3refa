from django.shortcuts import render
from main.models import Product
# Create your views here.

def get_product(request,id):
    product = Product.objects.get(pk=id)
    
<<<<<<< HEAD


   pass
=======
    return render(request,'shop-detail.html',{'product':product})
>>>>>>> dabd41447f1509f16a865b4d3209bc5c28040080

    