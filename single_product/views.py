from django.shortcuts import render
from main.models import Product
from django.contrib.auth.models import User,auth
# Create your views here.


    
def get_product(request,id):
    product = Product.objects.get(pk=id)


  
    return render(request,'shop-detail.html',{'product':product})

    
def review(request,id):
    product = Product.objects.get(pk=id)
    username= request.user.username
    product.rate = 4
    
    product.comment.append([username,request.POST['comment']])
    product.save()
    return render(request,'shop-detail.html',{'product':product})
