from django.urls import path
from . import views
urlpatterns =[
    path('', views.return_html_product , name='create_new_product'),
]