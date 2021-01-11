from django.urls import path
from . import views
urlpatterns =[
    path('', views.return_html_personal_shop , name='return_personal_shop'),
    path('<shop_name>', views.return_html_shop , name='return_html_shop'),
]