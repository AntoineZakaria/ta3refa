from django.urls import path
from . import views
urlpatterns =[
    path('', views.return_html_home , name='home'),
    path('shop_category/<category>', views.return_html_category, name='category'),
    path('verification/<code>', views.verify_code, name='verify_code')
]