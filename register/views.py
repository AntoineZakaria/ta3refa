from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from main.models import Person,Customer,Seller
from checkout.models import Cart
# Create your views here.
is_seller = False
shop_name = ""
def return_register(request):
    return render(request,'customer-register.html')
def login(request):
    if request.method== 'POST':
        username = request.POST['email_login']
        password = request.POST['password_login']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            logged_user_type = Person.objects.get(username=username)
            
            if logged_user_type.is_seller:
                is_seller = True
                seller = Seller.objects.get(username=username)
                shop_name= seller.shop_name
                messages.info(request, shop_name)
                return redirect('/dashboard')


            else:
                return redirect("/")
                 
        else:
            messages.info(request, 'incorrect User Name or password')
            return redirect('/')
    
    else:
        return render(request,'/register')


def logout(request):
    auth.logout(request)
    return redirect('/')

def customer_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        email= request.POST['email']
        password1= request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return redirect("/register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exists")
                return redirect("/register")
            else:
                person =Person(username=username,address=address,is_seller=False,Purchased_products=[])
                person.save()
                customer=Customer(username=username,rated_products=[],commented_products=[])
                customer.save()
                user = User.objects.create_user(username = username , email=email, password = password1, first_name=first_name,last_name=last_name)
                user.save();

                new_cart=Cart(user_id=User.objects.get(username=username).id,products=[])
                new_cart.save()

                messages.info(request,"user created you just need to Login")
            
        else:
            messages.info(request,"Password doesnt match")
            return redirect("register")
        return redirect('/')
    else:
        return render(request,'customer-register.html')




def seller_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        telephone = request.POST['phone']
        shop_name = request.POST['shop_name']
        address = request.POST['address']
        email= request.POST['email']
        password1= request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return redirect("/register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exists")
                return redirect("/register")
            else:
                person = Person(username=username,address=address,is_seller=True,Purchased_products=[])
                person.save()
                seller = Seller(username=username,shop_name=shop_name,telephone=telephone,owned_products=[])
                seller.save()
                user = User.objects.create_user(username = username , email=email, password = password1, first_name=first_name,last_name=last_name)
                user.save();
                messages.info(request,"Seller Account created . you just need to Login")
            
        else:
            messages.info(request,"Password doesnt match")
            return redirect("register")
        return redirect('/')
    else:
        return render(request,'customer-register.html')
        


