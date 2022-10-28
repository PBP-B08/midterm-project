from django.db import models

# Create your models here.
class Region(models.Model):
    nama = models.CharField(max_length=255)
    deskripsi = models.TextField()