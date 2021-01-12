from django.test import TestCase, Client
from django.urls import reverse
from main.models import Comment,Product,Person,Seller,Customer,mail_verification
from dashboard.models import Shop
import json
from django.contrib.auth.models import User,auth


class TestMainViews (TestCase):
    def setUp(self):
        self.client=Client()
        self.url_add=reverse('add_product')
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
        response=self.client.post(self.url_add,{
            'name':'product1',
            'category':'phones',
            'descrription':'test description',
            'price':100,
            'quantity':2,
            'offer':10,
            'photo1': open('test.png', 'rb')
        })
        response=self.client.post(self.url_add,{
            'name':'product1',
            'category':'phones',
            'descrription':'test description',
            'price':100,
            'quantity':2,
            'offer':10,
            'photo1': open('test.png', 'rb')
        })
        self.assertEquals(response.status_code,302)
        self.assertSequenceEqual(Product.objects.get(id=1).name,'product1')
        response=self.client.get(reverse('return_dashboard'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'dashboard_form.html')
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
        response=self.client.post(reverse('edit_product',args='1'),{
            'price':20,
            'quantity':10,
            'offer':50
        })
        self.assertEquals(response.status_code,302)
        self.assertEquals(Product.objects.get(id=1).price,20)
        self.assertEquals(Product.objects.get(id=1).quantity,10)
        self.assertEquals(Product.objects.get(id=1).offer,50)
        response=self.client.get(reverse('delete_product',args='3'))
        self.assertEquals(response.status_code,200)
        self.assertEquals(Product.objects.all().filter(id=3).exists(),False)
       





    




