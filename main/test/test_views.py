from django.test import TestCase, Client
from django.urls import reverse
from main.models import Comment,Product,Person,Seller,Customer,mail_verification
from django.contrib.auth.models import User,auth
import json
from django.contrib.auth.models import User,auth

class TestMainViews (TestCase):
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
            shop_name = 'tonyShop',
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
        self.url_home=reverse('home')#
        self.url_verify_code=reverse('verify_code',args=['tonytonytony'])
        self.url_category=reverse('category',args=['hiiiii'])
        self.url_redirect_to_main=reverse('redirect_to_main')
        self.url_favourite=reverse('favourite')
        self.url_filter=reverse('filter')
        self.url_add=reverse('add_product')
<<<<<<< HEAD


        self.url_login=reverse('login')
        response=self.client.post(self.url_login ,{
            'email_login':'tony',
            'password_login':'1234'
        })

=======
       
>>>>>>> 1a18528b3cd9f6ab95ea036809729baf4d08abce
    def test_home_get(self):
        response=self.client.get(self.url_home)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'shop-category-left.html')

    def test_verify_code(self):
        response=self.client.get(self.url_verify_code)
        self.assertEquals(response.status_code, 302)


    def test_category(self):
        response=self.client.get(self.url_category)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'shop-category.html')
    


    def test_redirect_to_main(self):
        response=self.client.get(self.url_redirect_to_main)
        self.assertEquals(response.status_code,302)
        




    def test_filter(self):
        response=self.client.get(self.url_filter,{
            'rate':5,
            'price_filter':1000

        })
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'filtered.html')



    def test_favourite(self):
        response=self.client.get(self.url_favourite)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'favourite.html')    


