from django.db import models

class Student(models.Model):
    sname=models.CharField(max_length=50)
    sage=models.IntegerField()
    saddress=models.CharField(max_length=50)
    spassword=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    cource=models.CharField(max_length=50)


# Create your models here.
