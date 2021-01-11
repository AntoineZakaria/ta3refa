from django.shortcuts import render
from main.models import Person,Customer,Seller,Product

# Create your views here.
def return_html_personal_shop(request):
    return render(request,'personal-shop.html')

def return_html_shop(request,shop_name):
    per= Seller.objects.get(username=shop_name)
    ar=per.owned_products
    prods=[]
    for item in ar:
        prods.append(Product.objects.get(pk=item))
    balance=per.current_balance
    return render(request,'shop_personal.html',{'prods':prods,'shop_name':shop_name})