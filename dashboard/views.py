from django.shortcuts import render , redirect
from main.models import Product

# Create your views here.
def return_dashboard(request):
    return render(request,'dashboard form.html')



def add_product(request):
    if request.method=='POST':
        name=request.POST['name']
        category=request.POST['category']
        description=request.POST['discription']
        price=request.POST['price']
        quantity=request.POST['quantity']
        img=request.POST['img']
        offer=request.POST['offer']
        new_product=Product(name=name,category=category,description=description,price=price,quantity=quantity,rate=0,offer=offer,comment=[],img=img,shop_id=0)
        new_product.save()
        return redirect('/')
        
def return_product():
    pass
        

