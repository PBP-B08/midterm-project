from django.db import models
from recommendation.models import Province

# Create your models here.
class Food(models.Model):
    # province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField(max_length = 255)
    
class Event(models.Model):
    # province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
    image = models.URLField(max_length = 255)