

from django.db import models

class PlanProperties(models.Model):
    destinasi = models.CharField(max_length=50)
    #tanggal = models.DateField()
    aktivitas = models.CharField(max_length=50)
    lokasi = models.CharField(max_length=50) 
    #jumlah_orang = models.IntegerField()
# Create your models here.


