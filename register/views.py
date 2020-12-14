from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from main.models import Person
# Create your views here.
def return_register(request):
    return render(request,'customer-register.html')
def login(request):
    if request.method== 'POST':
        email = request.POST['email_login']
        password = request.POST['password_login']

        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request,user)
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
                person =Person(first_name=first_name,last_name=last_name,address=address,email=email,is_seller=False,Purchased_products=[])
                person.save()
                user = User.objects.create_user(username = username , email=email, password = password1, first_name=first_name,last_name=last_name)
                user.save();
                messages.info(request,"user created")
            
        else:
            messages.info(request,"Password doesnt match")
            return redirect("register")
        return redirect('/')
    else:
        return render(request,'customer-register.html')