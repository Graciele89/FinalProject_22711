from django.db import models
import datetime
from django.utils import timezone
# from sorl.thumbnail import ImageField

class Post(models.Model):
    text_destination = models.CharField(max_length=140, blank=False, null=False)
    text_origin = models.CharField(max_length=140, blank=False, null=False)
    text_date = models.DateField(blank=False, null=False)
    text_time = models.TimeField(blank=False, null=False)

# class PostOffer(models.Model):
#     text_destination = models.CharField(max_length=140, blank=False, null=False)
#     text_origin = models.CharField(max_length=140, blank=False, null=False)
#     text_date = models.DateField(blank=False, null=False)
#     text_time = models.TimeField(blank=False, null=False)

    # image = ImageField()   //future implementation user upload his pic

    # def __str__(self):
    #     return self.text

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#     def __str__(self):
#         return self.question_text
#
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200, blank=False, null=False)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice_text
