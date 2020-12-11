from django.shortcuts import render
from main.models import Product
# Create your views here.


    
def get_product(request,id):
    product = Product.objects.get(pk=id)
    


  
    return render(request,'shop-detail.html',{'product':product})

    
