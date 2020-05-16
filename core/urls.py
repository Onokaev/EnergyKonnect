from django.urls import path, re_path, include
from django.conf.urls import url
from core import views
from . import views
from django.contrib import admin
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'transactions', views.TransactionViewSet)


urlpatterns = [
    path('', views.home, name='home'),
    path('appAPI/', include(router.urls)),
    path('apiAuth/', include('rest_framework.urls', namespace='rest_framework')),
    path('onoka/', views.onoka, name ='onoka')

]
