from django.db import models

# Create your models here.

class Speaker(models.Model):
    name=models.CharField(max_length=40)
    title=models.CharField(max_length=50)
    bio=models.CharField(max_length=10000)
    twitter=models.CharField(max_length=16,blank=True)
    facebook=models.CharField(max_length=50,blank=True)

     # returning name in site 
    def __str__(self):
        return self.name


class Track(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=1000)
    # returning name in site 
    def __str__(self):
        return self.title



class Sessions(models.Model):
    title=models.CharField(max_length=50)
    abstract=models.CharField(max_length=2000)
    track=models.ForeignKey(Track)
    speaker=models.ForeignKey(Speaker)
     # returning name in site 
    def __str__(self):
        return self.title

  





