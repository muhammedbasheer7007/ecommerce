from django.urls import path
from . import views
app_name='adminone'

urlpatterns=[
    path('home',views.adminone,name='home')
]