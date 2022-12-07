from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    decs=models.TextField()
class Team(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    decs = models.TextField()