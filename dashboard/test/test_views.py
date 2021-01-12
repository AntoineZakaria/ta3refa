from django.test import TestCase, Client
from django.urls import reverse
from main.models import Comment,Product,Person,Seller,Customer,mail_verification
from dashboard.models import Shop
import json
from django.contrib.auth.models import User,auth


class TestMainViews (TestCase):
    def setUp(self):
        self.client=Client()
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




