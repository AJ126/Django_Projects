from django.db import models

# Create your models here.
class data(models.Model):
    name=models.CharField(max_length=100)
    contact=models.IntegerField()
    address=models.CharField(max_length=500)
    order=models.CharField(max_length=5000)
    status=models.CharField(max_length=10)

class feedback(models.Model):
    name=models.CharField(max_length=50)
    feedback=models.CharField(max_length=100)
