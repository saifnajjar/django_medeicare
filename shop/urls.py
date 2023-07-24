from django.urls import path
from . import views


urlpatterns = [

path('CHECK_OUT/' , views.CHECK_OUT , name='CHECK_OUT'),
path('SHOP/' ,views.SHOP , name='SHOP'),
path('single_product/' ,views.single_product , name='single_product'),
path('YOUR_CART/' ,views.YOUR_CART , name='YOUR_CART'),


]