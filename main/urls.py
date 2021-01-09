from django.urls import path
from . import views
urlpatterns =[
    path('', views.return_html_home , name='home'),
    path('shop_category/<category>', views.return_html_category, name='category'),
    
    path('favourite', views.return_favourite, name='favourite')
   
   
]