from django import urls
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('register/', views.registerPage, name= 'register'),
        path('login/', views.loginPage, name= 'loginpage'),

]