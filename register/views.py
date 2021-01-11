from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from main.models import Person,Customer,Seller,mail_verification
import random
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from cryptography.fernet import Fernet
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
            exists_user = mail_verification.objects.all().filter(user_name=username).exists()
            if not(exists_user):
                file = open('my_dute_to_save.key' , 'rb')
                key = file.read()
                f= Fernet(key)
                random_code=random.random()
                random_code2='hgjkghjkhg'
                random_code = f.encrypt(str(random_code).encode())+f.encrypt(str(random_code2).encode())
                new_mail_verification=mail_verification(user_name=username,message_code=str(random_code),is_autonticated=False)
                new_mail_verification.save();
                message_to_send=f"https://73c61d0e2128.ngrok.io/verification/{str(random_code)}"
                print(message_to_send)
                send_mail(user.email,message_to_send)
                
                return redirect('/')

            elif (mail_verification.objects.get(user_name=username)).is_autonticated:
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
                messages.info(request, 'please verify your email')
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
                person =Person(username=username,address=address,is_seller=False,Purchased_products=[],favourite_products=[])
                person.save()
                customer=Customer(username=username,rated_products=[],commented_products=[])
                customer.save()
                user = User.objects.create_user(username = username , email=email, password = password1, first_name=first_name,last_name=last_name)
                user.save();
                messages.info(request,"user created you just need to check your email")
                #send mail ro verify
                file = open('my_dute_to_save.key' , 'rb')
                key = file.read()
                f= Fernet(key)
                random_code=random.random()
                random_code2='hgjkghjkhg'
                random_code = f.encrypt(str(random_code).encode())+f.encrypt(str(random_code2).encode())
                new_mail_verification=mail_verification(user_name=username,message_code=str(random_code),is_autonticated=False)
                new_mail_verification.save();
                message_to_send=f"https://73c61d0e2128.ngrok.io/verification/{str(random_code)}"
                print(message_to_send)
                send_mail(email,message_to_send)

                new_cart=Cart(user_id=User.objects.get(username=username).id,products=[])
                new_cart.save()

                #messages.info(request,"user created you just need to Login")
            
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
                person = Person(username=username,address=address,is_seller=True,Purchased_products=[],favourite_products=[])
                person.save()
                seller = Seller(username=username,shop_name=shop_name,telephone=telephone,owned_products=[],current_balance=0)
                seller.save()
                user = User.objects.create_user(username = username , email=email, password = password1, first_name=first_name,last_name=last_name)
                user.save();
                #send mail ro verify
                file = open('my_dute_to_save.key' , 'rb')
                key = file.read()
                f= Fernet(key)
                random_code=random.random()
                random_code2='hgjkghjkhg'
                random_code = f.encrypt(str(random_code).encode())+f.encrypt(str(random_code2).encode())
                new_mail_verification=mail_verification(user_name=username,message_code=str(random_code),is_autonticated=False)
                new_mail_verification.save();
                message_to_send=f"https://73c61d0e2128.ngrok.io/verification/{str(random_code)}"
                print(message_to_send)
                send_mail(email,message_to_send)
                messages.info(request,"Seller Account created . you just need to check your mail")

                new_cart=Cart(user_id=User.objects.get(username=username).id,products=[])
                new_cart.save()
            
        else:
            messages.info(request,"Password doesnt match")
            return redirect("register")
        return redirect('/')
    else:
        return render(request,'customer-register.html')
        


def send_mail(receiver_email,randm_link):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "tarefaa041@gmail.com"  # Enter your address
    password = '123456ytrewq'

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    your verification code
    from ta3refa"""
    html = f"""\
    <html>
    <body>
        <p>Hi,<br>
        How are you?<br>
        <button><a href="{randm_link}">click</a></button>
        has many great tutorials.
        </p>
    </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )