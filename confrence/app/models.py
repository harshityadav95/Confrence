from django.db import models

# Create your models here.

class Speaker(models.Model):
    name=models.CharField(max_length=40)
    title=models.CharField(max_length=50)
    bio=models.CharField(max_length=10000)

class Track(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=1000)


class Sessions(models.Model):
    title=models.CharField(max_length=50)
    abstract=models.CharField(max_length=2000)
    track=models.ForeignKey(Track)
    speaker=models.ForeignKey(Speaker)





