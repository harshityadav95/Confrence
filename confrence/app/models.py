from django.db import models

# Create your models here.

class Speaker(models.Model):
    name=models.CharField(max_length=40)
    title=models.CharField(max_length=50)
    bio=models.CharField(max_length=10000)

class Tracks(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=1000)




