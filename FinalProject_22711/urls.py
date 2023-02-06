from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from carpool import urls as carpool_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(carpool_urls, namespace='carpool')),
]
