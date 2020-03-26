from django.contrib import admin
from django.urls import path, include

#list of urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'))
]
