from django.urls import path
from .views import HomePageView, AddPostViewRequest, AddPostViewOffer, SeeRequests, DeleteRequestPost, SeeOffers, DeleteOffersPost
from . import views

app_name = 'carpool'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('post/<int:pk>', AddPostViewRequest.as_view(), name='post'), # url to my create request page
    path('offer/<int:pk>', AddPostViewOffer.as_view(), name='offer'),  # url to my create offer page
    path('requests/<int:pk>', SeeRequests.as_view(), name='requests'),   # url to see the created requests
    path('delete/<int:pk>', DeleteRequestPost.as_view(), name='delete'),  # path to delete requests done by user
    path('offers/<int:pk>', SeeOffers.as_view(), name='offers'),          # url to see the created offers  #}
    path('deleteOffers/<int:pk>', DeleteOffersPost.as_view(), name='deleteOffers')  # path to delete requests done by user
]
