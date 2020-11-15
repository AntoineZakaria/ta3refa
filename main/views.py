from django.shortcuts import render ,redirect
from django.contrib.auth.models import User , auth

# Create your views here.
def home (request):
    return render(request,'shop-category-full.html')