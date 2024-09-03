from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import about
from .models import client
from .models import contactform



def home(request):
    # aboutdata=about.objects.all()[1]
    aboutdata=about.objects.get(id=3)
    clientdata=client.objects.all()
    context={
        'about':aboutdata,
        'client':clientdata
        


    }
    return render (request,'index.html',context)
    #return HttpResponse('this is homepage')

def services (request):
    return render (request,'services.html')

def portfolio (request):
    return render (request,'portfolio.html')


def pricing (request):
    return render (request,'pricing.html')


def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contactformdata=contactform(name=name,email=email,subject=subject,message=message)
        contactformdata.save()

    
    return render(request,'contact.html')
