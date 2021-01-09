from django.shortcuts import render ,redirect
from django.contrib.auth.models import User , auth
from .models import Product
from . import views
import random

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
    
    #ya 4bab a3mlo add products ktyr 3l4an t4t8l
    #array_of_random_pr=random_products(3)   
    #prods = array_of_random_pr
    prods=Product.objects.all()

    return render(request,'shop-category-left.html',{'prods':prods})

def login(request):
    pass

def return_offer():
    pass



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






