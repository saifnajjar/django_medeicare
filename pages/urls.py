from django.urls import path
from . import views


urlpatterns = [

path('ABOUT/' , views.ABOUT , name='ABOUT'),
path('CONTACT_US/' , views.CONTACT_US , name='CONTACT_US'),

path('GALLERY/' , views.GALLERY , name='GALLERY'),

path('Home_Services/' , views.Home_Services , name='Home_Services'),




]