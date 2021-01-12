from django.test import TestCase, Client
from django.urls import reverse
from main.models import *
import json


class TestMainViews (TestCase):
    def setUp(self):
        self.client=Client()
        self.url_home=reverse('home')
        self.url_verify_code=reverse('verify_code',args=['tonytonytony'])
    def test_home_get(self):
        response=self.client.get(self.url_home)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'shop-category-left.html')
    def test_verify_code(self):
        response=self.client.get(self.url_verify_code)
        self.assertEquals(response.status_code, 302)



