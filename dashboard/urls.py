from django.urls import path
from . import views
urlpatterns =[
    path('', views.return_dashboard , name='return_dashboard'),
    path('/add_product', views.add_product , name='add_product'),
]