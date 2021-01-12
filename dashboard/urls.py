from django.urls import path
from . import views
urlpatterns =[
    path('', views.return_html_dashboard , name='return_dashboard'),
    path('add_product', views.add_product , name='add_product'),
    path('edit_product/<id>', views.edit_product , name='edit_product'),
    path('edit_product_view', views.return_edit_product , name='return_edit_product'),
    path('add_shop', views.add_shop , name='add_shop'),

    path('edit_shop/<id>', views.edit_shop , name='edit_shop'),
    path('edit_shop_view',views.return_edit_shop, name='return_edit_shop'),
    
   

    path('delete_shop/<id>', views.delete_shop , name='delete_shop'),
    path('delete_product/<id>', views.delete_product , name='delete_product'),

]