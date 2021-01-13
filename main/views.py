from django.shortcuts import render ,redirect
from django.contrib.auth.models import User , auth
from .models import Product 
from main.models import mail_verification
from .models import Person
from . import views
from checkout.models import Cart
import random
from django.http import HttpResponse
from django.contrib import messages

def return_html_category (request,category):
    prods= Product.objects.all().filter(category=category)

    ##prods=random_category_products(0,category)
 ## It takes the ammount of products you want .. im passing zero to avoid errors as you will not have products in your data base
    
    

    return render(request,'shop-category.html',{'prods':prods})



def return_html_home (request):
    """
    all that functions will be passed to front end
    #return_offers function
    #return_suggested function
    #return_random function
    #session user info
    """
    #####################################
    if request.user.is_authenticated:
        user_id = request.user.id
        np=0
        if not(Cart.objects.all().filter(user_id=user_id).exists()):
            new_cart=Cart(user_id=user_id,products=[])
            new_cart.save()
        user_cart=Cart.objects.get(user_id=user_id)
        products=[]
        for i in user_cart.products:
            np=np+1
            
        request.session['np']=np
    else:
        request.session['np']=0
    #####################################
    
    #ya 4bab a3mlo add products ktyr 3l4an t4t8l
    #array_of_random_pr=random_products(3)   
    #prods = array_of_random_pr
    prods=Product.objects.all()
    if request.user.is_authenticated:
        current_username=request.user.username
        per= Person.objects.get(username=current_username)
        dash_flag=per.is_seller
    else:
        dash_flag=False

    return render(request,'shop-category-left.html',{'prods':prods,'dash_flag':dash_flag})




def random_products(range_product):
    #range_product -> number of products in the random products array
    array_of_random_pr = []
    for i in range(range_product):
        flag = 1
        while len(array_of_random_pr) < range_product:
            random_object = Product.objects.all()[random.randint(0, Product.objects.count() - 1)]
            for single_product in array_of_random_pr:
                if single_product == random_object:
                    flag = 0
            if flag:        
                array_of_random_pr.append(random_object)
    return array_of_random_pr



def random_category_products(range_product,category):
    #range_product -> number of products in the random products array
    array_of_random_pr = []
    for i in range(range_product):
        flag = 1
        while len(array_of_random_pr) < range_product:
            random_object = Product.objects.all().filter(category=category)[random.randint(0, Product.objects.filter(category=category).count() - 1)]
            for single_product in array_of_random_pr:
                if single_product == random_object:
                    flag = 0
            if flag:        
                array_of_random_pr.append(random_object)
    return array_of_random_pr


def verify_code(request,code):
    verification_email=mail_verification.objects.all().filter(message_code=code).exists()
    if verification_email== False:
        messages.info(request, 'that code is not available')
        return redirect('/')

    else:
        verification_email=mail_verification.objects.get(message_code=str(code))
        verification_email.is_autonticated=True
        verification_email.save();
        messages.info(request, 'your account has been verified you can login now')
        return redirect('/')




def return_favourite(request):
    if request.user.is_authenticated:
        current_username=request.user.username
        per= Person.objects.get(username=current_username)
        dash_flag=per.is_seller
    else:
        dash_flag=False
    current_username=request.user.username
    per= Person.objects.get(username=current_username)
    list_products=per.favourite_products
    prods=[]
    for item in list_products:
        p=Product.objects.all().filter(category=item)
        for single in p:
            prods.append(single)
       
    return render(request,'favourite.html',{'prods':prods,'dash_flag':dash_flag})

def redirect_to_main(request):
    if not(Person.objects.all().filter(username=request.user.username).exists()):
        person =Person(username=request.user.username,address="fady",is_seller=False,Purchased_products=[],favourite_products=[])
        person.save()
    return redirect('/')



def return_filter(request):
    rate = request.GET['rate']
    price_filter = request.GET['price_filter']
    #prods=Product.objects.filter(rate__gte = rate)
    if (rate == 'none'):
        if (price_filter == 1000):
            prods=Product.objects.filter(price__lte = 1000 )
        
        elif (float(price_filter) < 6000 and price_filter!=1000):
            prods = Product.objects.filter(price__lte = float(price_filter) , price__gte = float(price_filter)-999)
        else:
            prods = Product.objects.filter(price__gte = float(price_filter)+1)


    else:
        if (price_filter == 1000):
            prods=Product.objects.filter(price__lte = 1000 ,rate__gte = rate )
            
        elif (float(price_filter) < 6000 and price_filter!=1000):
            prods = Product.objects.filter(price__lte = float(price_filter) , rate__gte = rate, price__gte = float(price_filter)-999)
        else:
            prods = Product.objects.filter(price__gte = float(price_filter)+1, rate__gte = rate)


    return render(request,'filtered.html',{'prods':prods})  




def return_how_to_use(request):
    return render(request,'how_to_use.html')      