from django.db import models


# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
class student2(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)

class student3(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)

