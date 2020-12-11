from django.urls import path
from . import views
urlpatterns =[
<<<<<<< HEAD
    path('', views.return_html_product , name='create_new_product'),
=======
    path('show_product/<id>', views.get_product , name='get_product'),
>>>>>>> 6d8a6ffbc4a658040d3a9bf508d36347bac503ee
]