from django.db import models

# Create your models here.

class emp(models.Model):
    name = models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    salary=models.IntegerField()
    status=models.BooleanField()




