from django.shortcuts import render

# Create your views here.

def return_html_product(request):
    return render(request,'shop-detail.html')