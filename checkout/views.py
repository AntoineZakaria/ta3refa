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
        single_prod.quantity=single_prod.quantity-1
        single_prod.save()
        sellerid=single_prod.shop_id
        theseller=Seller.objects.get(pk=sellerid)
        theseller.current_balance=theseller.current_balance+product_price
        theseller.save()
    if request.method == 'POST':
        Shipping = request.POST['Shipping']
        Payment = request.POST['Payment']
    if request.user.email =="":
        pass
    else:
        send_mail(request.user.email,products,Shipping,Payment)
    
    user_cart=Cart.objects.get(user_id=user_id)
    user_cart.products=[]
    user_cart.save()
    request.session['np']=0
    
    return redirect('/')


  
   






def cart_page (request):
    #return_shop_list function
    #stripe_pay function
    #send_mail_details
    #calculate_pay
    #####################################
    if request.user.is_authenticated:
        user_id = request.user.id
        np=0
        if not(Cart.objects.all().filter(user_id=user_id).exists()):
            new_cart=Cart(user_id=user_id,products=[])
            new_cart.save()
        user_cart=Cart.objects.get(user_id=user_id)
        products=[]
        for i in user_cart.products:
            np=np+1
            
        request.session['np']=np
    else:
        request.session['np']=0
    #####################################
    if request.user.is_authenticated:
        current_username=request.user.username
        per= Person.objects.get(username=current_username)
        dash_flag=per.is_seller
    else:
        dash_flag=False
    user_id = request.user.id
    user_cart=Cart.objects.get(user_id=user_id)
    products=[]
    for i in user_cart.products:
        products.append(Product.objects.get(pk=i))
    totalprice=calc_cart(user_cart.products)    
   

    return render(request,'shop-basket.html',{'products':products,'totalprice':totalprice,'dash_flag':dash_flag})

def add_to_cart(request,id):
    user_id = request.user.id
    np=0
    if not(Cart.objects.all().filter(user_id=user_id).exists()):
        new_cart=Cart(user_id=user_id,products=[])
        new_cart.save()
    user_cart=Cart.objects.get(user_id=user_id)
    user_cart.products.append(Product.objects.get(pk=id).pk)
    user_cart.save()
    products=[]
    for i in user_cart.products:
        np=np+1
        products.append(Product.objects.get(pk=i))
    request.session['np']=np
    totalprice=calc_cart(user_cart.products)    
   

    return redirect('/checkout/')

def remove_from_cart(request,id):
    request.session['np']=int(request.session['np'])-1
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



def send_mail(receiver_email,products,Shipping,Payment):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "tarefaa041@gmail.com"  # Enter your address
    password = '123'

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email
    text_viko=""
    sum_invoice=0
    taxes=0
    if Shipping=="Standard":
        taxes=50
    elif Shipping=="Express":
        taxes=100

    for single_prod in products:
        text_viko=text_viko+f"""\
                <tr class="item">
                <td>
                    {single_prod.name}
                </td>
                
                <td>
                   {single_prod.new_price()}
                </td>
                </tr>\n
            """
        sum_invoice=sum_invoice+single_prod.new_price()
    # Create the plain-text and HTML version of your message
    text = """\
    your verification code
    from ta3refa"""
    html = f"""\
        <!doctype html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>A simple, clean, and responsive HTML invoice template</title>
            
            <style>
            .invoice-box {{
                max-width: 800px;
                margin: auto;
                padding: 30px;
                border: 1px solid #eee;
                box-shadow: 0 0 10px rgba(0, 0, 0, .15);
                font-size: 16px;
                line-height: 24px;
                font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
                color: #555;
            }}
            
            .invoice-box table {{
                width: 100%;
                line-height: inherit;
                text-align: left;
            }}
            
            .invoice-box table td {{
                padding: 5px;
                vertical-align: top;
            }}
            
            .invoice-box table tr td:nth-child(2) {{
                text-align: right;
            }}
            
            .invoice-box table tr.top table td {{
                padding-bottom: 20px;
            }}
            
            .invoice-box table tr.top table td.title {{
                font-size: 45px;
                line-height: 45px;
                color: #333;
            }}
            
            .invoice-box table tr.information table td {{
                padding-bottom: 40px;
            }}
            
            .invoice-box table tr.heading td {{
                background: #eee;
                border-bottom: 1px solid #ddd;
                font-weight: bold;
            }}
            
            .invoice-box table tr.details td {{
                padding-bottom: 20px;
            }}
            
            .invoice-box table tr.item td{{
                border-bottom: 1px solid #eee;
            }}
            
            .invoice-box table tr.item.last td {{
                border-bottom: none;
            }}
            
            .invoice-box table tr.total td:nth-child(2) {{
                border-top: 2px solid #eee;
                font-weight: bold;
            }}
            
            @media only screen and (max-width: 600px) {{
                .invoice-box table tr.top table td {{
                    width: 100%;
                    display: block;
                    text-align: center;
                }}
                
                .invoice-box table tr.information table td {{
                    width: 100%;
                    display: block;
                    text-align: center;
                }}
            }}
            
            /** RTL **/
            .rtl {{
                direction: rtl;
                font-family: Tahoma, 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
            }}
            
            .rtl table {{
                text-align: right;
            }}
            
            .rtl table tr td:nth-child(2) {{
                text-align: left;
            }}
            </style>
        </head>
        <body>
            <div class="invoice-box">
                <table cellpadding="0" cellspacing="0">
                    <tr class="top">
                        <td colspan="2">
                            <table>
                                <tr>
                                    <td class="title">
                                        <img src="https://i.ibb.co/vQF34SR/logota3refa.png" style="width:100%; max-width:300px;">
                                    </td>
                                    
                                    
                                </tr>
                            </table>
                        </td>
                    </tr>    
                    <tr class="information">
                        <td colspan="2">
                        
                                    <h2>Order Details</h2>
                                    </td>
                            
                    </tr>
                    <tr class="heading">
                        <td>
                            Payment Method
                        </td>
                        
                      
                    </tr>         
                    <tr class="details">
                        <td>
                            {Payment}
                        </td>        
                      
                    </tr>
                    <tr class="heading">
                        <td>
                            Shipping Method
                        </td>
                        
                        <td>
                            Shipping cost
                        </td>
                    </tr>         
                    <tr class="details">
                        <td>
                            {Shipping}
                        </td>        
                        <td>
                            {taxes}
                        </td>
                    </tr>
                    
                    <tr class="heading">
                        <td>
                            Item
                        </td>
                        
                        <td>
                            Price
                        </td>
                    </tr>
                    {text_viko}
                    <tr class="total">
                        <td></td>
                        
                        <td>
                        Total: {sum_invoice+taxes} $
                        </td>
                    </tr>
                </table>
            </div>
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
        server.sendmail(sender_email, receiver_email, message.as_string())
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