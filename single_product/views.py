from django.shortcuts import render, redirect
from main.models import Product
from django.contrib.auth.models import User,auth
from main.models import Person
from django.http import HttpResponseRedirect
# Create your views here.


    
def get_product(request,id):
    product = Product.objects.get(pk=id)
    if request.user.is_authenticated:
        current_username=request.user.username
        per= Person.objects.get(username=current_username)
        if not ((product.category) in (per.favourite_products)):
            per.favourite_products.append(product.category)
            per.save()
 

  
    return render(request,'shop-detail.html',{'product':product})

    
def review(request,id):
    product = Product.objects.get(pk=id)
    username= request.user.username
    user_rate =0
    
    if "rating" in request.POST:
        user_rate +=1
    if "rating2" in request.POST:
        user_rate =2
    if "rating3" in request.POST:
        user_rate =3
    if "rating4" in request.POST:
        user_rate =4
    if "rating5" in request.POST:
        user_rate =5

    product.comment.append([username,int(user_rate),request.POST['comment']])
    product.save()
    ## calculate overall ratinggggggggggggggggg
    prod = Product.objects.get(pk=id)
    count = 0
    rates = 0
    produc_overall_rate =0

    for comment in prod.comment:
        one_rate = int(comment[1])
        rates += one_rate
        count +=1
    produc_overall_rate = rates / count
    prod.rate = produc_overall_rate
    prod.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

