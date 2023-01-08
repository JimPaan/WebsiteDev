from django.db import models


# Create your models here.


class BusData1(models.Model):
    jaja = models.CharField(max_length=100)
    numPass = models.IntegerField()
    eta = models.IntegerField()
