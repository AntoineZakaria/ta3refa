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
        User.objects.create(
            username='tony',
            email='tony.felo18@gmail.com',
            password='1234',
            is_superuser=False,
            first_name='antonios',
            last_name='amgad',
            is_staff=False,
            is_active=True
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
        self.url_verify_code=reverse('review',args=[1])

    def test_get_product(self):
        response=self.client.get(self.url_get_product)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'shop-detail.html')

    def test_review(self):
        response = self.client.get(self.url_review)
        self.assertEquals(response.status_code,302)
