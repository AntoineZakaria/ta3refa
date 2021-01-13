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
                new_mail_verification.save()
                message_to_send=f"https://a331eae7648b.ngrok.io/verification/{str(random_code)}"
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
                new_mail_verification.save()
                message_to_send=f"https://a331eae7648b.ngrok.io/verification/{str(random_code)}"
                print(message_to_send)
                send_mail(email,message_to_send)

                new_cart=Cart(user_id=User.objects.get(username=username).id,products=[])
                new_cart.save()

                #messages.info(request,"user created you just need to Login")
            
        else:
            messages.info(request,"Password doesnt match")
            return redirect("/register")
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
                user.save()
                #send mail ro verify
                file = open('my_dute_to_save.key' , 'rb')
                key = file.read()
                f= Fernet(key)
                random_code=random.random()
                random_code2='hgjkghjkhg'
                random_code = f.encrypt(str(random_code).encode())+f.encrypt(str(random_code2).encode())
                new_mail_verification=mail_verification(user_name=username,message_code=str(random_code),is_autonticated=False)
                new_mail_verification.save();
                message_to_send=f"https://a331eae7648b.ngrok.io/verification/{str(random_code)}"
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
    sender_email = "ta3refa0000@gmail.com"  # Enter your address
    password = 'TONY1234'

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = "verification code"
    html = f"""\
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml">
        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <title>Verify your email address</title>
        <style type="text/css" rel="stylesheet" media="all">
            /* Base ------------------------------ */
            *:not(br):not(tr):not(html) {{
            font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;
            -webkit-box-sizing: border-box;
            box-sizing: border-box;
            }}
            body {{
            width: 100% !important;
            height: 100%;
            margin: 0;
            line-height: 1.4;
            background-color: #F5F7F9;
            color: #839197;
            -webkit-text-size-adjust: none;
            }}
            a {{
            color: #414EF9;
            }}

            /* Layout ------------------------------ */
            .email-wrapper {{
            width: 100%;
            margin: 0;
            padding: 0;
            background-color: #F5F7F9;
            }}
            .email-content {{
            width: 100%;
            margin: 0;
            padding: 0;
            }}

            /* Masthead ----------------------- */
            .email-masthead {{
            padding: 25px 0;
            text-align: center;
            }}
            .email-masthead_logo {{
            max-width: 400px;
            border: 0;
            }}
            .email-masthead_name {{
            font-size: 16px;
            font-weight: bold;
            color: #839197;
            text-decoration: none;
            text-shadow: 0 1px 0 white;
            }}

            /* Body ------------------------------ */
            .email-body {{
            width: 100%;
            margin: 0;
            padding: 0;
            border-top: 1px solid #E7EAEC;
            border-bottom: 1px solid #E7EAEC;
            background-color: #FFFFFF;
            }}
            .email-body_inner {{
            width: 570px;
            margin: 0 auto;
            padding: 0;
            }}
            .email-footer {{
            width: 570px;
            margin: 0 auto;
            padding: 0;
            text-align: center;
            }}
            .email-footer p {{
            color: #839197;
            }}
            .body-action {{
            width: 100%;
            margin: 30px auto;
            padding: 0;
            text-align: center;
            }}
            .body-sub {{
            margin-top: 25px;
            padding-top: 25px;
            border-top: 1px solid #E7EAEC;
            }}
            .content-cell {{
            padding: 35px;
            }}
            .align-right {{
            text-align: right;
            }}

            /* Type ------------------------------ */
            h1 {{
            margin-top: 0;
            color: #292E31;
            font-size: 19px;
            font-weight: bold;
            text-align: left;
            }}
            h2 {{
            margin-top: 0;
            color: #292E31;
            font-size: 16px;
            font-weight: bold;
            text-align: left;
            }}
            h3 {{
            margin-top: 0;
            color: #292E31;
            font-size: 14px;
            font-weight: bold;
            text-align: left;
            }}
            p {{
            margin-top: 0;
            color: #839197;
            font-size: 16px;
            line-height: 1.5em;
            text-align: left;
            }}
            p.sub {{
            font-size: 12px;
            }}
            p.center {{
            text-align: center;
            }}

            /* Buttons ------------------------------ */
            .button {{
            display: inline-block;
            width: 200px;
            background-color: #414EF9;
            border-radius: 3px;
            color: white;
            font-size: 15px;
            line-height: 45px;
            text-align: center;
            text-decoration: none;
            -webkit-text-size-adjust: none;
            mso-hide: all;
            }}
            .button--green {{
            background-color: #28DB67;
            }}
            .button--red {{
            background-color: #FF3665;
            }}
            .button--blue {{
            background-color: #414EF9;
            }}

            /*Media Queries ------------------------------ */
            @media only screen and (max-width: 600px) {{
            .email-body_inner,
            .email-footer {{
                width: 100% !important;
            }}
            }}
            @media only screen and (max-width: 500px) {{
            .button {{
                width: 100% !important;
            }}
            }}
        </style>
        </head>
        <body>
        <table class="email-wrapper" width="100%" cellpadding="0" cellspacing="0">
            <tr>
            <td align="center">
                <table class="email-content" width="100%" cellpadding="0" cellspacing="0">
                <!-- Logo -->
                <tr>
                    <td class="email-masthead">
                    <a class="email-masthead_name">ta3refa</a>
                    </td>
                </tr>
                <!-- Email Body -->
                <tr>
                    <td class="email-body" width="100%">
                    <table class="email-body_inner" align="center" width="570" cellpadding="0" cellspacing="0">
                        <!-- Body content -->
                        <tr>
                        <td class="content-cell">
                            <h1>Verify your email address</h1>
                            <p>Thanks for signing up for ta3refa! We're excited to have you as an early user.</p>
                            <!-- Action -->
                            <table class="body-action" align="center" width="100%" cellpadding="0" cellspacing="0">
                            <tr>
                                <td align="center">
                                <div>
                                    <!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="{{action_url}}" style="height:45px;v-text-anchor:middle;width:200px;" arcsize="7%" stroke="f" fill="t">
                                    <v:fill type="tile" color="#414EF9" />
                                    <w:anchorlock/>
                                    <center style="color:white;font-family:sans-serif;font-size:15px;">Verify Email</center>
                                </v:roundrect><![endif]-->
                                    <a href="{randm_link}" class="button button--green">Verify Email</a>
                                    
                                </div>
                                </td>
                            </tr>
                            </table>
                            <p>Thanks,<br>The ta3refa Team</p>
                            <!-- Sub copy -->
                            <table class="body-sub">
                            <tr>
                                <td>
                                <p class="sub">If you’re having trouble clicking the button, copy and paste the URL below into your web browser.
                                </p>
                                <p class="sub"><a href="{randm_link}">{randm_link}</a></p>
                                </td>
                            </tr>
                            </table>
                        </td>
                        </tr>
                    </table>
                    </td>
                </tr>
                <tr>
                    <td>
                    <table class="email-footer" align="center" width="570" cellpadding="0" cellspacing="0">
                        <tr>
                        <td class="content-cell">
                            <p class="sub center">
                            ta3refa Labs, Inc.
                            <br>325 9th St, San Francisco, CA 94103
                            </p>
                        </td>
                        </tr>
                    </table>
                    </td>
                </tr>
                </table>
            </td>
            </tr>
        </table>
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