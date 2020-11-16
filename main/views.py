from django.shortcuts import render ,redirect
from django.contrib.auth.models import User , auth


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
    return render(request,'shop-category-full.html')

def login(request):
    pass
def logout(request):
    pass

