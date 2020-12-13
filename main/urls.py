from django.urls import path
from . import views
urlpatterns =[
    path('', views.return_html_home , name='home')
   
   
]