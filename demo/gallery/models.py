from django.db import models

class Gallery(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=255)

class Photo(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=255)
    gallery = models.ForeignKey(Gallery)
    
