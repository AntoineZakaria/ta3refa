from django.test import TestCase, Client
from django.urls import reverse
from main.models import Comment,Product,Person,Seller,Customer,mail_verification
from django.contrib.auth.models import User,auth
import json

class TestRegister(TestCase):
    def setUp(self):
        self.client=Client()
        self.url_get_product=reverse('get_product',args=[1])
        self.url_review = reverse('review' , args=[1])
        self.client=Client()
      
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

    def test_return_reg(self):
        self.url_reg = reverse('return_register')
        response=self.client.get(self.url_get_product)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'shop-detail.html')

    def test_customer_reg(self):
        self.url_customer_reg = reverse('customer_register')
        response=self.client.post(self.url_customer_reg,{
            'username':'tony',
            'email':'antwanemile@gmail.com',
            'address':'myaddress1',
            'password1':'1234',
            'password2':'1234',
            'is_superuser':False,
            'first_name':'tony',
            'last_name':'em',
            'is_staff':False,
            'is_active':True
        })

        self.assertEquals(Person.objects.get(username='tony').is_seller , False)
        self.assertEquals(response.status_code,302)

    def test_seller_reg(self):
        self.url_customer_reg = reverse('seller_register')
        response=self.client.post(self.url_customer_reg,{
            'username':'tonySeller',
            'email':'antwan@gmail.com',
            'phone': '0123456789',
            'shop_name' : 'Sadidas',
            'address':'myaddress1',
            'password1':'1234',
            'password2':'1234',
            'is_superuser':False,
            'first_name':'antwan',
            'last_name':'Emil',
            'is_staff':False,
            'is_active':True
        })
        self.assertEquals(Person.objects.get(username='tonySeller').is_seller , True)
        self.assertEquals(response.status_code,302)

    def test_login(self):
        self.url_login=reverse('login')
        response=self.client.get(self.url_get_product)
        response=self.client.post(self.url_login,{
            'email_login':'tony',
            'password_login':'1234',
        }
        )
        self.assertEquals(response.status_code,302)
    def test_logout(self):
        self.url_logout = reverse('logout')
        response=self.client.get(self.url_get_product)
        self.assertEquals(response.status_code,200)