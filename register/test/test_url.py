from django.test import SimpleTestCase
from django.urls import resolve,reverse
from register.views import return_register,customer_register,seller_register,login,logout
class TestMainUrls(SimpleTestCase):
    def test_return_register_url_resolves(self):
        url=reverse('return_register')
        self.assertEquals(resolve(url).func,return_register)
    def test_customer_register_url_resolves(self):
        url=reverse('customer_register')
        self.assertEquals(resolve(url).func,customer_register)
    def test_seller_register_url_resolves(self):
        url=reverse('seller_register')
        self.assertEquals(resolve(url).func,seller_register)
    def test_login_url_resolves(self):
        url=reverse('login')
        self.assertEquals(resolve(url).func,login)
    def test_logout_url_resolves(self):
        url=reverse('logout')
        self.assertEquals(resolve(url).func,logout)
