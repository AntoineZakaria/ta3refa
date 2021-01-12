from django.test import TestCase, Client
from django.urls import reverse
from checkout.models import Cart
import json
from django.contrib.auth.models import User,auth
from main.models import Person,Seller,mail_verification,Product


class TestCheckoutViews (TestCase):
    def setUp(self):

        self.client=Client()
        
        User.objects.create_user(
            id=1,
            username='tony',
            email='tony.felo18@gmail.com',
            password='1234',
            is_superuser=True,
            first_name='antonios',
            last_name='amgad',
            is_staff=True,
            is_active=True,
            date_joined='2021-01-11 16:49:26.898785+02'
        )
        Person.objects.create(
            id=1,
            username='tony',
            address='ADDRESS1',
            is_seller=True,
            Purchased_products=[],
            favourite_products=[]
        )
        Seller.objects.create(
            id=1,
            username='tony',
            shop_name = 'shop1_test',
            telephone = 123, 
            owned_products = [],
            current_balance = 0
        )
        mail_verification.objects.create(
        user_name= 'tony',
        message_code='TEST',
        is_autonticated=True
        )



        self.url_login=reverse('login')
        response=self.client.post(self.url_login ,{
            'email_login':'tony',
            'password_login':'1234'
        })


        self.cart=Cart.objects.create(
            user_id=1,
            products=[]
            
           
        )
        Product.objects.create(
            id=1,
            name="prod",
            description="desc",
            price= 100,
            quantity=5,
            rate = 3,
            offer = 1,
            img= "product_image/bridge_dVtWd1W.jpg",
            comment = [['tony',1,"good"]],
            shop_id="1",
            category="Phones"
        )
       
        self.cart_page_url=reverse('cart_page')
        self.complete_purchase_url=reverse('complete_purchase')
        self.add_to_cart_url=reverse('add_to_cart',args=["1"])
        self.remove_from_cart_url=reverse('remove_from_cart',args=["1"])




    def test_add_to_cart(self):
        response=self.client.get(self.add_to_cart_url)
        self.assertEquals(response.status_code,302)
         
       
    def test_complete_purchase(self):
        response=self.client.post(self.complete_purchase_url,{
            'Shipping':'Standard',
            'Payment':'Cash On Delivery'
        })
        self.assertEquals(response.status_code, 302)    

        
    def test_cart_page(self):
        response=self.client.get(self.cart_page_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'shop-basket.html')


   
    def test_remove_from_cart(self):
        response=self.client.get(self.add_to_cart_url)
        self.assertEquals(response.status_code,302)
    
    
    
    
    



