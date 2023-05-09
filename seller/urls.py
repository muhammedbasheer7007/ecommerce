from django.urls import path
from . import views
app_name='seller'

urlpatterns=[
    path('home',views.seller,name='home')
]