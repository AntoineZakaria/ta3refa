from django.urls import path
from . import views
urlpatterns =[
    path('customer-register.html',views.register , name='customer-register.html')
]