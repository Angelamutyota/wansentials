from wansentialsapp.views import profile
from django.contrib import admin
from django.urls.conf import include
from .models import Profile, Product, Orderedproduct, Order

# Register your models here.
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Orderedproduct)
admin.site.register(Order)