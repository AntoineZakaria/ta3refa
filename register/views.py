from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def login(request):
    if request.method== 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request, 'incorrect username or password')
            return redirect('customer-register.html')
    
    else:
        return render(request,'customer-register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        username = request.POST['name-login']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        email= request.POST['email']
        telephone = request.POST['phone']
        password1= request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return redirect("customer-register.html")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exists")
                return redirect("customer-register.html")
            else:
                user = User.objects.create_user(username = username ,address=address,phone=telephone, email=email, password = password1, first_name=first_name,last_name=last_name)
                user.save();
                messages.info(request,"user created")
            
        else:
            messages.info(request,"Password doesnt match")
            return redirect("customer-register")
        return redirect('/')
    else:
        return render(request,'customer-register.html')