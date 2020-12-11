from django.shortcuts import render , redirect
from main.models import Product
from .models import Shop

# Create your views here.
def return_dashboard(request):
    return render(request,'dashboard_form.html')



def add_product(request):
    if request.method=='POST':
        name=request.POST['name']
        category=request.POST['category']
        description=request.POST['descrription']
        price=request.POST['price']
        quantity=request.POST['quantity']
        img=request.POST['img']
        offer=request.POST['offer']
        new_product=Product(name=name,category=category,description=description,price=price,quantity=quantity,rate=0,offer=offer,comment=[],img=img,shop_id=0)
        new_product.save()
        return redirect('/')
        
def add_shop(request):
    if request.method=='POST':
        shop_name=request.POST['shop_name']
        facebook_seller=request.POST['facebook_seller']
        gmail_seller=request.POST['gmail_seller']
        website_seller=request.POST['website_seller']
        phonenumber=request.POST['phonenumber']
        addrress=request.POST['addrress']
        method_of_received_money=request.POST['method_of_received_money']
        new_shop=Shop(shop_name=shop_name,
        facebook_seller=facebook_seller,
        gmail_seller=gmail_seller,
         website_seller= website_seller,
         mainshop_owner=0,
         phonenumber=phonenumber,
         admins=[],
         products=[],
         addrress=addrress,
         shop_money=0,
         method_of_received_money=method_of_received_money)
        new_shop.save()
        return redirect('/')
        

