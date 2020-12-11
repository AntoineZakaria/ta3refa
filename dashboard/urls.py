from django.urls import path
from . import views
urlpatterns =[
    path('', views.return_html_dashboard , name='return_dashboard'),
    path('add_product', views.add_product , name='add_product'),
    path('edit_product/<id>', views.edit_product , name='edit_product'),
    path('edit_product_view', views.return_edit_product , name='return_edit_product'),
    path('add_shop', views.add_shop , name='add_shop'),
   
]