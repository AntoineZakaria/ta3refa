from django.shortcuts import render
from main.models import Person,Customer,Seller,Product
from checkout.models import Cart
# Create your views here.
def return_html_personal_shop(request):
    return render(request,'personal-shop.html')

def return_html_shop(request,shop_name):
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
            products.append(Product.objects.get(pk=i))
        request.session['np']=np
    else:
        request.session['np']=0
    #####################################

    per= Seller.objects.get(shop_name=shop_name)
    ar=per.owned_products
    prods=[]
    for item in ar:
        prods.append(Product.objects.get(pk=item))
    balance=per.current_balance
    return render(request,'shop_personal.html',{'prods':prods,'shop_name':shop_name})