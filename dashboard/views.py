from django.shortcuts import render , redirect
from main.models import Product
from main.models import Seller
from .models import Shop
from django.http import HttpResponseRedirect
# Create your views here.

def return_html_dashboard(request):
    current_username=request.user.username
    per= Seller.objects.get(username=current_username)
    ar=per.owned_products
    prods=[]
    for item in ar:
        prods.append(Product.objects.get(pk=item))
    return render(request,'dashboard_form.html',{'prods':prods})

def return_edit_product(request):
    return render(request,'try_edit_product.html')

############
def return_edit_shop(request):
    return render(request,'try_edit_shop.html')
############

def add_product(request):
    if request.method=='POST':
        name=request.POST['name']
        category=request.POST['category']
        description=request.POST['descrription']
        price=request.POST['price']
        quantity=request.POST['quantity']
        img=request.FILES['photo1']
        offer=request.POST['offer']
        shop_id = request.user.id
        if offer =='':
            offer=0
        new_product=Product(name=name,category=category,description=description,price=price,quantity=quantity,rate=0,offer=offer,comment=[],img=img,shop_id=shop_id)
        new_product.save()
        current_username=request.user.username
        per= Seller.objects.get(username=current_username)
        per.owned_products.append(new_product.id)
        per.save()
        return redirect('/dashboard')
        

def edit_product(request, id):
    edit_product = Product.objects.get(pk=id)
    if request.method == 'POST':
        edit_product.price=request.POST['price']
        edit_product.quantity=request.POST['quantity']
        edit_product.offer=request.POST['offer']
        edit_product.save()
    return redirect('/dashboard')

        

def delete_product(request,id):
    current_username=request.user.username
    per= Seller.objects.get(username=current_username)
    ar=per.owned_products
    ar.remove(id)
    per.save() 
    Product.objects.filter(pk=id).delete()
    prods=[]
    for item in ar:
        prods.append(Product.objects.get(pk=item))
    return render(request,'dashboard_form.html',{'prods':prods})


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

def edit_shop(request, id):
    edit_shop = Shop.objects.get(pk=id)
    if request.method=='POST':
        edit_shop.shop_name=request.POST['shop_name']
        edit_shop.facebook_seller=request.POST['facebook_seller']
        edit_shop.gmail_seller=request.POST['gmail_seller']
        edit_shop.website_seller=request.POST['website_seller']
        edit_shop.phonenumber=request.POST['phonenumber']
        edit_shop.addrress=request.POST['addrress']
        edit_shop.method_of_received_money=request.POST['method_of_received_money']
        edit_shop.save()
        return redirect('/')


