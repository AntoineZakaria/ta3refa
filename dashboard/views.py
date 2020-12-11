from django.shortcuts import render , redirect
from main.models import Product
from .models import Shop

# Create your views here.

def return_html_dashboard(request):
    return render(request,'dashboard_form.html')

def return_edit_product(request):
    return render(request,'try_edit_product.html')

def add_product(request):
    if request.method=='POST':
        name=request.POST['name']
        category=request.POST['category']
        description=request.POST['descrription']
        price=request.POST['price']
        quantity=request.POST['quantity']
        img=request.FILES['photo1']
        offer=request.POST['offer']
        new_product=Product(name=name,category=category,description=description,price=price,quantity=quantity,rate=0,offer=offer,comment=[],img=img,shop_id=0)
        new_product.save()
        return redirect('/')
        

def edit_product(request, id):
    edit_product = Product.objects.get(pk=id)
    if request.method == 'POST':
        edit_product.name=request.POST['name']
        edit_product.category=request.POST['category']
        edit_product.description=request.POST['descrription']
        edit_product.price=request.POST['price']
        edit_product.quantity=request.POST['quantity']
        edit_product.img=request.POST['img']
        edit_product.offer=request.POST['offer']
        edit_product.save()
        return redirect('/')

def delete_product(request,id):
    Product.objects.filter(pk=id).delete()
    return redirect('/')

def delete_shop(request,id):
    Shop.objects.filter(pk=id).delete()
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
        

