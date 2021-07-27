from wansentialsapp.views import profile
from django.contrib import admin
from django.urls.conf import include
from .models import Profile

# Register your models here.
admin.site.register(Profile)