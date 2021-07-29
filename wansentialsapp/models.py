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
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)


    @classmethod
    def search_by_name(cls,search_term):
        product = cls.objects.filter(name__icontains=search_term)
        return product

    def __str__(self):
        return f'{self.name}'

class Orderedproduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)

   