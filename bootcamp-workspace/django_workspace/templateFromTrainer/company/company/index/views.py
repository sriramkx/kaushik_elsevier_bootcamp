from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')
    #return HttpResponse('this is homepage')

def services (request):
    return render(request, 'services.html')
    #return HttpResponse('this is services ')

def portfolio (request):
    return render(request, 'portfolio.html')
    #return HttpResponse('this is portfolio ')


def pricing (request):
    return render(request, 'pricing.html')
    #return HttpResponse('this is pricing ')


def contact (request):
    return render(request, 'contact.html')
    #return HttpResponse('this is contact ')