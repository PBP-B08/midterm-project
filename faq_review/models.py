from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class reviewUser(models.Model):
    user = models.ForeignKey(User ,on_delete = models.CASCADE)
    date_add = models.DateField()
    title = models.TextField()
    review = models.TextField()

class FrequentlyAskedQuestion(models.Model):
    question = models.TextField()
    answer = models.TextField()

    