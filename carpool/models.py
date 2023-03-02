from django.contrib.auth.models import User
from django.db import models
import datetime
from django.utils import timezone
# from sorl.thumbnail import ImageField


class Post(models.Model):
    text_destination = models.CharField(max_length=140, blank=False, null=False)
    text_origin = models.CharField(max_length=140, blank=False, null=False)
    text_date = models.DateField(blank=False, null=False)
    text_time = models.TimeField(blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)




class PostOffer(models.Model):
    text_destination = models.CharField(max_length=140, blank=False, null=False)
    text_origin = models.CharField(max_length=140, blank=False, null=False)
    text_date = models.DateField(blank=False, null=False)
    text_time = models.TimeField(blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # image = ImageField()   //future implementation user upload his pic


