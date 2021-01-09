from django.shortcuts import render
from main.models import Product
from main.models import Person
# Create your views here.


    
def get_product(request,id):
    product = Product.objects.get(pk=id)
    current_username=request.user.username
    per= Person.objects.get(username=current_username)
    if not ((product.category) in (per.favourite_products)):
     per.favourite_products.append(product.category)
     per.save()
 

  
    return render(request,'shop-detail.html',{'product':product})

    
