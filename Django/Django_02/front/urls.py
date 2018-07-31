from django.urls import path
from . import views

# app name space

app_name = 'front'

urlpatterns =[
    path('', views.index, name='index'),
    path('login/', views.login, name='login')
]