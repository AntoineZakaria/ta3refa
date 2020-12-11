from django.urls import path
from . import views
urlpatterns =[
    path('', views.home , name='home'),
    path('customer-register.html',views.signup , name='customer-register.html'),
    path('dashboard_form.html',views.dashboard , name='dashboard')
   
]