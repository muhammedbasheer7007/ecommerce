from django.urls import path
from . import views
app_name='buyer'

urlpatterns=[
    path('home',views.buyer,name='home')
]