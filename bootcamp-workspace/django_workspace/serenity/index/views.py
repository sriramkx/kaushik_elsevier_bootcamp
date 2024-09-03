from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')
    #return HttpResponse('this is home page')

def services(request):
    return render(request,'services.html')
    #return HttpResponse('this is services page')

def portfolio(request):
    return render(request,'portfolio.html')
    #return HttpResponse('this is portfolio page')

def pricing(request):
    return render(request,'pricing.html')
    #return HttpResponse('this is pricing page')

def blog(request):
    return render(request,'blog.html')
    #return HttpResponse('this is blog page')

def contact(request):
    return render(request,'contact.html')
    #return HttpResponse('this is contact page')