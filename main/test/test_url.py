from django.test import SimpleTestCase
from django.urls import resolve,reverse
from main.views import return_html_category,return_html_home,verify_code,return_favourite,redirect_to_main,return_filter
class TestUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url=reverse('home')
        self.assertEquals(resolve(url).func,return_html_home)
    def test_shop_cat_url_resolves(self):
        url=reverse('category')
        self.assertEquals(resolve(url).func,return_html_category)