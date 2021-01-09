from django.shortcuts import render ,redirect
from django.contrib.auth.models import User , auth



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
    return render(request,'shop-basket.html')    


