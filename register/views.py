from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def register(request):
    if request.method == 'POST':
        name = request.POST['name-login']
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
                user = User.objects.create_user(username = name ,address=address,phone=telephone, email=email, password = password1)
                user.save();
                messages.info(request,"user created")
        else:
            messages.info(request,"Password doesnt match")
            return redirect("customer-register")
        return redirect('/')
    else:
        return render(request,'customer-register.html')