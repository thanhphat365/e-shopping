from django.db import models
from django.contrib.auth.models import User   
# Create your models here.
class Post( models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.CharField(max_length=10)
    image = models.CharField( max_length=300,blank=True, null=True)
    def __str__(self):
        return self.title
class User(models.Model):
    name = models.CharField(max_length=100)
    
