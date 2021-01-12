from django.test import SimpleTestCase
from django.urls import resolve,reverse
from single_product.views import get_product,review

class TestSingle_productsUrls(SimpleTestCase):
    def test_single_product_get_product(self):
        url=reverse('get_product',args=[1])
        self.assertEquals(resolve(url).func,get_product)
    def test_single_product_review(self):
        url = reverse('review',args=[1])
        self.assertEquals(resolve(url).func,review)