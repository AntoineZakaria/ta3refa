from django.urls import path
from . import views
urlpatterns =[
    path('', views.return_dashboard , name='return_dashboard'),
]