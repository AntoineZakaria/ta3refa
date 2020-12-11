from django.urls import path
from . import views
urlpatterns =[
    
    path('/show_product/<id>', views.get_product , name='get_product'),
]