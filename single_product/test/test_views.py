from django.test import TestCase, Client
from django.urls import reverse
from single_product.models import *
from main.models import Product
import json


class TestSingle_productViews (TestCase):
    def setUp(self):
        self.client=Client()
        self.url_get_product=reverse('get_product')
        self.url_verify_code=reverse('get_product',args=[1])
        Product.objects.create{
            id=1,
            name="22",
        }
        self.url_verify_code=reverse('review',args=[1])

    def test_get_product(self):
        response=self.client.get(self.url_get_product)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'shop-detail.html')