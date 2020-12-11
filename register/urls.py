from django.urls import path
from . import views
urlpatterns =[
    path('',views.return_register , name='return_register'),
    path('customer_register' , views.customer_register, name= 'customer_register'),
    path("login" , views.login , name="login"),
    path("logout", views.logout , name= "logout")
]