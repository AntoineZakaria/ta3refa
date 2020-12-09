from django.shortcuts import render ,redirect
from django.contrib.auth.models import User , auth
from .models import Product
from . import views

def return_offers():
    pass
def return_suggested():
    pass
def return_random():
    pass



def home (request):
    """
    all that functions will be passed to front end
    #return_offers function
    #return_suggested function
    #return_random function
    #session user info
    """
    prods = Product.objects.all()

    return render(request,'shop-category-left.html',{'prods':prods})

def login(request):
    pass
def logout(request):
    pass
def return_offer():
    pass


def signup(request):
    return render(request,'customer-register.html')


