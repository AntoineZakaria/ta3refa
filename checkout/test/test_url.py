from django.test import SimpleTestCase
from django.urls import resolve,reverse
from checkout.views import cart_page,add_to_cart,remove_from_cart,complete_purchase
class TestUrls(SimpleTestCase):
    def test_cart_page_url_resolves(self):
        url=reverse('cart_page')
        self.assertEquals(resolve(url).func,cart_page)
   
   
   
   
    def test_complete_purchase_url_resolves(self):
        url=reverse('complete_purchase')
        self.assertEquals(resolve(url).func,complete_purchase)
    
    
    
    
    def test_add_to_cart_resolves(self):
        url=reverse('add_to_cart',args=['some-slug'])
        self.assertEquals(resolve(url).func,add_to_cart)
    
    
    
    
    
    def test_remove_from_cart_url_resolves(self):
        url=reverse('remove_from_cart',args=['some-slug'])
        self.assertEquals(resolve(url).func,remove_from_cart)    