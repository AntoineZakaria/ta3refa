from django.urls import path
from . import views
urlpatterns =[
    path('', views.return_personal_shop , name='return_personal_shop'),
]