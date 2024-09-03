from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    text = {'name':'Check'}
    return render (request,'index.html', text)
    #return HttpResponse('this is homepage')

def services (request):
    return render (request,'services.html')

def portfolio (request):
    return render (request,'portfolio.html')


def pricing (request):
    return render (request,'pricing.html')


def contact (request):
    return render (request,'contact.html')