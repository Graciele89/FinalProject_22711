from django.urls import path
from .views import HomePageView, AddPostViewRequest, AddPostViewOffer, SeeRequests, DeleteRequestPost
from . import views

app_name = 'carpool'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('post/<int:pk>', AddPostViewRequest.as_view(), name='post'),
    path('offer/', AddPostViewOffer.as_view(), name='offer'),
    path('requests/<int:pk>', SeeRequests.as_view(), name='requests'),
    path('delete/<int:pk>', DeleteRequestPost.as_view(), name='delete')
]
