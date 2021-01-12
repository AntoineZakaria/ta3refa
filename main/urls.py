from django.urls import path
from . import views
urlpatterns =[
    path('', views.return_html_home , name='home'),
    path('shop_category/<category>', views.return_html_category, name='category'),
    path('verification/<code>', views.verify_code, name='verify_code'),
    path('accounts/profile/', views.redirect_to_main, name='redirect_to_main'),
    
    path('favourite', views.return_favourite, name='favourite'),
    path('filter', views.return_filter, name='filter')

   
   
]