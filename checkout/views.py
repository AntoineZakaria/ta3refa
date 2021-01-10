from django.shortcuts import render ,redirect
from django.contrib.auth.models import User , auth
from .models import Cart
from main.models import Product, Seller,Person




def return_shop_list ():
    pass

def stripe_pay ():
    pass

def calculate_pay ():
    pass

def send_mail_details ():
    pass

def cart_page (request):
    #return_shop_list function
    #stripe_pay function
    #send_mail_details
    #calculate_pay
    user_id = request.user.id
    user_cart=Cart.objects.get(user_id=user_id)
    products=[]
    for i in user_cart.products:
        products.append(Product.objects.get(pk=i))

    totalprice=calc_cart(user_cart.products)    
   

    return render(request,'shop-basket.html',{'products':products,'totalprice':totalprice})

def add_to_cart(request,id):
    user_id = request.user.id
    user_cart=Cart.objects.get(user_id=user_id)
    user_cart.products.append(Product.objects.get(pk=id).pk)
    user_cart.save()
    products=[]
    for i in user_cart.products:
        products.append(Product.objects.get(pk=i))

    totalprice=calc_cart(user_cart.products)    
   

    return redirect('/checkout/')

def remove_from_cart(request,id):
    user_id = request.user.id
    user_cart=Cart.objects.get(user_id=user_id)
    user_cart.products.remove(id)
    user_cart.save()
    products=[]
    for i in user_cart.products:
        products.append(Product.objects.get(pk=i))

    totalprice=calc_cart(user_cart.products)    
   

    return  redirect('/checkout/')               


def calc_cart(products):
    sum=0
    for i in products:
        sum=sum+Product.objects.get(pk=i).new_price()
    return sum 

def give_vendors_money(request,id):
    user_id = request.user.id
    user_cart=Cart.objects.get(user_id= user_id)
    products = user_cart.products
    #product= Product.objects.get(pk=product_id)
    for product_id in products:
        product = Product.objects.get(id=product_id)
        shop_id = int(product.shop_id) 
        shop = Seller.objects.get(id = int(shop_id))
        shop.balance += product.new_price()
        shop.save()
            
    return redirect('/')