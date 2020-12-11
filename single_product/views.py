from django.shortcuts import render
from main.models import Product
# Create your views here.

def get_product(request,id):
    


    return render(request,'shop-detail.html',{'product':product)

    