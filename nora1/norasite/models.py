from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_title = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.topic_title
    
class webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    url = models.URLField(unique=True)
    webpage_title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.webpage_title
    
class accessrecord(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    
    
class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    date = models.DateField()
    
    