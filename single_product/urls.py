from django.urls import path
from . import views
urlpatterns =[
    path('', views.return_html_product , name='create_new_product'),
    path('show_product/<id>', views.get_product , name='get_product'),
]