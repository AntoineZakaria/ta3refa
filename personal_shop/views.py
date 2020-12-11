from django.shortcuts import render

# Create your views here.
def return_html_personal_shop(request):
    return render(request,'personal-shop.html')

