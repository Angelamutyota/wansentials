from django import urls
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('register/', views.registerPage, name= 'register'),
        path('login/', views.loginPage, name= 'loginpage'),
        path('logout/',views.logoutpage,name='logout'),

        path('',views.index, name = 'index'),
        path('profile/', views.profile, name= 'profile'),
        path('updateprofile/', views.update_profile, name= 'updateprofile'),
        path('search/', views.search_results, name='search_results'),
        path('product/<int:id>/',views.product,name='product'),
        path('checkout/', views.checkout, name= 'checkout'),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)