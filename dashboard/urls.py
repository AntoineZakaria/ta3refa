from django.urls import path
from . import views
urlpatterns =[
<<<<<<< HEAD
    path('', views.return_html_dashboard , name='return_dashboard'),
=======
    path('', views.return_dashboard , name='return_dashboard'),
    path('/add_product', views.add_product , name='add_product'),
>>>>>>> 6d8a6ffbc4a658040d3a9bf508d36347bac503ee
]