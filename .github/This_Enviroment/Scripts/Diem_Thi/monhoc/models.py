from django.db import models

class monhoc(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  dcc = models.FloatField(max_length=2)
  dthi = models.FloatField(max_length=2)
  dtb = models.FloatField(max_length=2)
  t4 = models.FloatField(max_length=2)
  result = models.CharField(max_length=255)