from django.urls import path
from . import views
urlpatterns =[
    path('', views.card_page , name='card_page'),
]