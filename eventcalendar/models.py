from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField('Location Name', max_length=75)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField('Event Name',max_length=250)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    event_date = models.DateField('Event Date')
    #admin_author = models.ManyToMany
    
    def __str__(self):
        return self.title