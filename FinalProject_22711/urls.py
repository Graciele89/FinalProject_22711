from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic.base import TemplateView

from carpool import urls as carpool_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(carpool_urls, namespace='carpool')),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
