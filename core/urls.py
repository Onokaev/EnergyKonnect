from django.urls import path, re_path
from django.conf.urls import url
from core import views
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('karanja/', views.karanja)
    #request for token 
]
