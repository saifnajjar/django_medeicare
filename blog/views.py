from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def BLOG_GRID(request):
    return render(request, 'BLOG/BLOG_GRID.html')



def BLOG_LIST(request):
    return render(request, 'BLOG/BLOG_LIST.html')


def SINGLE_POST(request):
    return render(request, 'BLOG/SINGLE_POST.html')    






