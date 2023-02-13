from django.urls import path
from .views import HomePageView
from . import views

app_name = 'carpool'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
]
