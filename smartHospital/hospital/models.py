from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Doctor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    hospital = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,null=False,default="",unique=True)
    password = models.CharField(max_length=30,null=False,default="")
    def __str__(self):
        return self.first_name

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100,null=False,default="",unique=True)
    password = models.CharField(max_length=40,null=False,default="")

    def __str__(self):
        return self.first_name
