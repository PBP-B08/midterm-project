

from django.db import models
from django.contrib.auth.models import User

class PlanProperties(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    judul = models.CharField(max_length=50)
    destinasi = models.CharField(max_length=150)
    #tanggal = models.DateField()
    aktivitas = models.CharField(max_length=50)
    hari = models.IntegerField()
    orang = models.IntegerField()
    deskripsi = models.TextField()
    #jumlah_orang = models.IntegerField()
# Create your models here.


