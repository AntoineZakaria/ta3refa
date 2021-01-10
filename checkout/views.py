from django.shortcuts import render ,redirect
from django.contrib.auth.models import User , auth
from .models import Cart
from main.models import Product ,Seller,Person
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart




def return_shop_list ():
    pass

def stripe_pay ():
    pass

def calculate_pay ():
    pass

def send_mail_details ():
    pass

def complete_purchase(request):
    user_id = request.user.id
    user_cart=Cart.objects.get(user_id=user_id)
    products=[]
    for i in user_cart.products:
        products.append(Product.objects.get(pk=i))
    for single_prod in products:
        product_price=single_prod.new_price()
        sellerid=single_prod.shop_id
        theseller=Seller.objects.get(pk=sellerid)
        theseller.current_balance=theseller.current_balance+product_price
        theseller.save()
    send_mail(request.user.email,products)
    user_cart=Cart.objects.get(user_id=user_id)
    user_cart.products=[]
    user_cart.save()
    
    return redirect('/')


  
   






def cart_page (request):
    #return_shop_list function
    #stripe_pay function
    #send_mail_details
    #calculate_pay
    user_id = request.user.id
    user_cart=Cart.objects.get(user_id=user_id)
    products=[]
    for i in user_cart.products:
        products.append(Product.objects.get(pk=i))
    totalprice=calc_cart(user_cart.products)    
   

    return render(request,'shop-basket.html',{'products':products,'totalprice':totalprice})

def add_to_cart(request,id):
    user_id = request.user.id
    user_cart=Cart.objects.get(user_id=user_id)
    user_cart.products.append(Product.objects.get(pk=id).pk)
    user_cart.save()
    products=[]
    for i in user_cart.products:
        products.append(Product.objects.get(pk=i))

    totalprice=calc_cart(user_cart.products)    
   

    return redirect('/checkout/')

def remove_from_cart(request,id):
    user_id = request.user.id
    user_cart=Cart.objects.get(user_id=user_id)
    user_cart.products.remove(id)
    user_cart.save()
    products=[]
    for i in user_cart.products:
        products.append(Product.objects.get(pk=i))

    totalprice=calc_cart(user_cart.products)    
   

    return  redirect('/checkout/')               


def calc_cart(products):
    sum=0
    for i in products:
        sum=sum+Product.objects.get(pk=i).new_price()
    return sum 



def send_mail(receiver_email,products):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "Ta3refa00@gmail.com"  # Enter your address
    password = 'TONY12345'

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email
    text_viko=""
    for single_prod in products:
        text_viko=text_viko+f"<h1>{single_prod.name}</h1>"
    # Create the plain-text and HTML version of your message
    text = """\
    your verification code
    from ta3refa"""
    html = f"""\
    <html>
    <body>
        <p>Hi,<br>
        list products<br>
        {text_viko}
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
"""
def give_vendors_money(request,id):
    user_id = request.user.id
    user_cart=Cart.objects.get(user_id= user_id)
    products = user_cart.products
    #product= Product.objects.get(pk=product_id)
    for product_id in products:
        product = Product.objects.get(id=product_id)
        shop_id = int(product.shop_id) 
        shop = Seller.objects.get(id = int(shop_id))
        shop.balance += product.new_price()
        shop.save()
            
    return redirect('/')
"""