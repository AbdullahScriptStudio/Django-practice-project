from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class UserInfoModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    #extra fields we want
    linkedin_link = models.URLField(max_length=200, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    
    #function to display the info when object in printed
    def __str__(self):
        return self.user.username
    



class User_model(models.Model):
    f_name = models.CharField (max_length= 100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.f_name + ' ' + self.l_name