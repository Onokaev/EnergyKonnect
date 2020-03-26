from django.urls import path, re_path
from django.conf.urls import url
from core import views
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('onoka/', views.onoka, name ='onoka'),
    path('consumption_update/<meter>/<latest_consumed>/<units_remaining>/', views.consumption_update, name ='consumption_update'), #update from the meter
    path('units_balance/<meter>/', views.units_balance, name = 'units_balance')   #request for token balance from mobile app 
]
