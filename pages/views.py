from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


    
def ABOUT(request):
    return render(request, 'pages/ABOUT.html')



def Home_Services(request):
    return render(request, 'pages/Home_Services.html')

def CONTACT_US(request):
    return render(request, 'pages/CONTACT_US.html')


def GALLERY(request):
    return render(request, 'pages/GALLERY.html')





    

    




