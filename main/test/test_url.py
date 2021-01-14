from django.test import SimpleTestCase
from django.urls import resolve,reverse
from main.views import return_html_category,return_html_home,verify_code,return_favourite,redirect_to_main,return_filter,return_how_to_use
class TestMainUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url=reverse('home')
        self.assertEquals(resolve(url).func,return_html_home)
    def test_redirect_to_main_url_resolves(self):
        url=reverse('redirect_to_main')
        self.assertEquals(resolve(url).func,redirect_to_main)
    def test_return_favourite_url_resolves(self):
        url=reverse('favourite')
        self.assertEquals(resolve(url).func,return_favourite)
    def test_return_filter_url_resolves(self):
        url=reverse('filter')
        self.assertEquals(resolve(url).func,return_filter)

    def test_return_how_to_use(self):
        url=reverse('how_to_use')
        self.assertEquals(resolve(url).func,return_how_to_use)
    def test_shop_cat_url_resolves(self):
        url=reverse('category',args=['some_slug'])
        self.assertEquals(resolve(url).func,return_html_category)
    def test_verify_code_url_resolves(self):
        url=reverse('verify_code',args=['some_slug'])
        self.assertEquals(resolve(url).func,verify_code)