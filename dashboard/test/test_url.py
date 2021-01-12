from django.test import SimpleTestCase
from django.urls import resolve,reverse
from dashboard.views import return_html_dashboard,add_product,edit_product,return_edit_product,add_shop,edit_shop,return_edit_shop,delete_product,delete_shop
class TestUrls(SimpleTestCase):
    def test_return_html_dashboard_url_resolves(self):
        url=reverse('return_dashboard')
        self.assertEquals(resolve(url).func,return_html_dashboard)
   
   
   
   
    def test_add_product_url_resolves(self):
        url=reverse('add_product')
        self.assertEquals(resolve(url).func,add_product)
    
    
    
    
    def test_edit_product_url_resolves(self):
        url=reverse('edit_product',args=['some-slug'])
        self.assertEquals(resolve(url).func,edit_product)
    
    
    
    
    
    def test_return_edit_product_url_resolves(self):
        url=reverse('return_edit_product')
        self.assertEquals(resolve(url).func,return_edit_product)




    def test_add_shop_url_resolves(self):
        url=reverse('add_shop')
        self.assertEquals(resolve(url).func,add_shop) 


    def test_edit_shop_url_resolves(self):
        url=reverse('edit_shop',args=['some-slug'])
        self.assertEquals(resolve(url).func,edit_shop)



    def test_return_edit_shop_url_resolves(self):
        url=reverse('return_edit_shop')
        self.assertEquals(resolve(url).func,return_edit_shop)    



    def test_delete_shop_url_resolves(self):
        url=reverse('delete_shop',args=['some-slug'])
        self.assertEquals(resolve(url).func,delete_shop)



    def test_delete_product_url_resolves(self):
        url=reverse('delete_product',args=['some-slug'])
        self.assertEquals(resolve(url).func,delete_product)    
