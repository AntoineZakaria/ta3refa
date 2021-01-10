from django.urls import path
from . import views
urlpatterns =[
    path('', views.cart_page , name='cart_page'),
    path('add_to_cart/<id>', views.add_to_cart, name='add_to_cart'),
     path('remove_from_cart/<id>', views.remove_from_cart, name='remove_from_cart'),
     path('finishing/<id>', views.give_vendors_money, name='finishing')
]