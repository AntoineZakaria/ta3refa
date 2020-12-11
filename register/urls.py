from django.urls import path
from . import views
urlpatterns =[
    path('customer-register.html',views.register , name='customer-register.html'),
    path("login" , views.login , name="login"),
    path("logout", views.logout , name= "logout")
]