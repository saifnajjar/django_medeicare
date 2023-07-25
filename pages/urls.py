from django.urls import path
from . import views


urlpatterns = [


path('CONTACT_US/' , views.CONTACT_US , name='CONTACT_US'),

path('GALLERY/' , views.GALLERY , name='GALLERY'),






]