from django.test import TestCase, Client
from django.urls import reverse
from main.models import Comment,Product,Person,Seller,Customer,mail_verification
from checkout.models import Cart
import json
from django.contrib.auth.models import User,auth

class TestPersonal_shop(TestCase):
    def setUp(self):
        self.client=Client()
        self.url_html_personal_shop=reverse('return_personal_shop')
        self.url_html_shop = reverse('return_html_shop',args=['shop1_test'])
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
            Purchased_products=[1,2],
            favourite_products=[]
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
            comment = [],
            shop_id="1",
            category="Phones"
        )
        Seller.objects.create(
            id=1,
            username='tony',
            shop_name = 'shop1_test',
            telephone = 123, 
            owned_products = ["1"],
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
        

    def test_html_personal_shop(self):
        response=self.client.get(self.url_html_personal_shop)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'personal-shop.html')

    def test_html_shop(self):
         response=self.client.get(self.url_html_shop)
         self.assertEquals(response.stats_code,200)
         self.assertTemplateUsed(response,'shop_personal.html')


