from django.urls import path
from django.conf.urls import url
from core import views
from . import views
from django.contrib import admin

urlpatterns = [
    path('kplc.herokuapp.com/', views.home, name='home'),

    #request for token 
]
