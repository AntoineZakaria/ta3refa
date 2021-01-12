from django.test import SimpleTestCase
from django.urls import resolve,reverse
from personal_shop.views import return_html_shop,return_html_personal_shop

class TestPersonal_shopUrls(SimpleTestCase):
    def test_personal_shop_return_html_personal_shop(self):
        url= reverse('return_personal_shop')
        self.assertEquals(resolve(url).func, return_html_personal_shop)
    def test_personal_shop_return_html_shop(self):
        url= reverse('return_html_shop',args=['A'])
        self.assertEquals(resolve(url).func,return_html_shop)
