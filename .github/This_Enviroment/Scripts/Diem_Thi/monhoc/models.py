from django.db import models

class monhoc(models.Model):
  studentID = models.FloatField(max_length=10)
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  dcc = models.IntegerField()
  dthi = models.IntegerField()
  dtb = models.IntegerField()
  t4 = models.IntegerField()
  result = models.CharField(max_length=10)