from django.urls import path
from django.conf.urls import url
from core import views
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),

    #request for token 
]
