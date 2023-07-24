
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def CHECK_OUT(request):
    return render(request, 'shop/CHECK_OUT.html')



def SHOP(request):
    return render(request, 'shop/SHOP.html')


def single_product(request):
    return render(request, 'shop/single_product.html') 


def YOUR_CART(request):
    return render(request, 'shop/YOUR_CART.html')        


   

# Create your views here.
# Create your views here.
