from django.urls import path
from . import views
urlpatterns =[
<<<<<<< HEAD
    path('', views.return_dashboard , name='return_dashboard'),
    path('add_product', views.add_product , name='add_product'),
    path('add_shop', views.add_shop , name='add_shop'),
=======
    path('', views.return_html_dashboard , name='return_dashboard'),
    path('/add_product', views.add_product , name='add_product'),
>>>>>>> b11fee3a2afad126e5fb765697fdd98efe5264f6
]