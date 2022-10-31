from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class reviewUser(models.Model):
    user = models.ForeignKey(User ,on_delete = models.CASCADE)
    date_add = models.DateField(default = timezone.now)
    title = models.TextField()
    review = models.TextField()

class FrequentlyAskedQuestion(models.Model):
    question = models.TextField()
    answer = models.TextField()

    