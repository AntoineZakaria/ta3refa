from django.test import TestCase, Client
from django.urls import reverse
from main.models import Comment,Product,Person,Seller,Customer,mail_verification
import json
from django.contrib.auth.models import User,auth


class TestMainViews (TestCase):
    def setUp(self):
        self.client=Client()
        self.url_home=reverse('home')#
        self.url_verify_code=reverse('verify_code',args=['tonytonytony'])
        self.url_category=reverse('category',args=['hiiiii'])
        self.url_redirect_to_main=reverse('redirect_to_main')
        self.url_favourite=reverse('favourite')
        self.url_filter=reverse('filter')
        self.url_add=reverse('add_product')
        self.url_html_personal_shop=reverse('return_personal_shop')
        self.url_html_shop = reverse('return_html_shop',args=['tony'])
        self.url_how_to_use=reverse('how_to_use')
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
        Seller.objects.create(
            id=1,
            username='tony',
            shop_name = 'tony',
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
        response=self.client.get(self.url_home)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'shop-category-left.html')
        response=self.client.get(self.url_verify_code)
        self.assertEquals(response.status_code, 302)
        response=self.client.get(self.url_category)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'shop-category.html')
        response=self.client.get(self.url_redirect_to_main)
        self.assertEquals(response.status_code,302)
        response=self.client.get(self.url_filter,{
            'rate':5,
            'price_filter':1000

        })
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'filtered.html')
        response=self.client.get(self.url_favourite)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'favourite.html')    

        response=self.client.get(self.url_html_personal_shop)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'personal-shop.html')

        response=self.client.get(self.url_html_shop)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'shop_personal.html')
        response=self.client.get(self.url_how_to_use,{
            'current_username':'tony'
        })
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'how_to_use.html') 