from django.db import models

# Create your models here.
class Food(models.Model):
    # daerah = models.ForeignKey()
    nama = models.CharField(max_length=255)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='files/food')
    
class Event(models.Model):
    # daerah = models.ForeignKey()
    nama = models.CharField(max_length=255)
    tanggal = models.DateField()
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='files/events')