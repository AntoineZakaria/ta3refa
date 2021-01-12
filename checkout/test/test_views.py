from django.test import TestCase, Client
from django.urls import reverse
from checkout.models import Cart
import json


class TestCheckoutViews (TestCase):
    def setUp(self):
        self.client=Client()
        self.cart_page_url=reverse('cart_page')
      #  self.url_verify_code=reverse('verify_code',args=['tonytonytony'])
    def test_cart_page(self):
        response=self.client.get(self.cart_page_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'shop-basket.html')
   # def test_verify_code(self):
    #    response=self.client.get(self.url_verify_code)
     #   self.assertEquals(response.status_code, 302)



