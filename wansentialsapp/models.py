from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=80, blank=True)
    bio = models.TextField(max_length=254, blank=True)
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='images/', default='default.png')

    def __str__(self):
        return f'{self.user.username} profile'

class Product(models.Model):
    name = models.CharField(max_length=80, blank=True)
    picture = models.ImageField(upload_to='images/', default='default.png')
    description = models.TextField()
    price = models.CharField(max_length = 10,blank =True)

    def __str__(self):
                return f'{self.name}'
