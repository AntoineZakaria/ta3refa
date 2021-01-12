from django.test import TestCase, Client
from django.urls import reverse
from main.models import Comment,Product,Person,Seller,Customer,mail_verification
from django.contrib.auth.models import User,auth
import json


class TestSingle_productViews (TestCase):
    def setUp(self):
        self.client=Client()
        self.url_get_product=reverse('get_product',args=[1])
        self.url_review = reverse('review' , args=[1])
        self.client=Client()
        User.objects.create_user(
            username='tony',
            email='tony.felo18@gmail.com',
            password='1234',
            is_superuser=False,
            first_name='antonios',
            last_name='amgad',
            is_staff=False,
            is_active=True
        )
        Person.objects.create(
            username='tony',
            address='ADDRESS1',
            is_seller=True,
            Purchased_products=[],
            favourite_products=[]
        )
        Seller.objects.create(
            username='tony',
            shop_name = 'shop1_test',
            telephone = 123, 
            owned_products = [],
            current_balance = 0
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
        #self.url_verify_code=reverse('review',args=[1])
    print(Product)
    def test_login(self):
        self.url_login=reverse('login')
        response=self.client.post(self.url_login,{
            'email_login':'tony',
            'password_login':'1234',
        }
        )
        self.assertEquals(response.status_code,302)
        
    def test_get_product(self):
        response=self.client.get(self.url_get_product)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'shop-detail.html')
      
    def test_review(self):
          #giving the product rate=1
        response = self.client.post(self.url_review,{'username':"tony",'comment':"bad",'rating':True})
        self.assertEquals(response.status_code,302)
        #testing the overall rating 
        self.assertEquals(Product.objects.get(name='prod').rate , 1)
        #Testing If the comment has been added proberly
        self.assertEquals(Product.objects.get(name='prod').comment[1][1] , '1')
        self.assertEquals(Product.objects.get(name='prod').comment[1][2] , "bad")
         
