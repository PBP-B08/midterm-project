from django.db import models
from recommendation.models import Province

# Create your models here.

class EventCalendar(models.Model):
    title = models.CharField('Event Name',max_length=250)
    description = models.TextField()
    location = models.ForeignKey(Province, on_delete=models.CASCADE)
    event_date = models.DateField('Event Date')
    
    def __str__(self):
        return self.title