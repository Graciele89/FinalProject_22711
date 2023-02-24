from django.urls import path
from .views import HomePageView, AddPostView
from . import views

app_name = 'carpool'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('post/', AddPostView.as_view(), name='post'),
]
