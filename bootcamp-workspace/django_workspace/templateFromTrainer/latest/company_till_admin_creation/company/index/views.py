from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import about
from .models import pricingModel
from .models import clientsModel
from .models import contactform

def home(request):
    #text={'name':'priya',
    #'friends':['lucy','smith']}
    #return render (request,'index.html',text)
    #return HttpResponse('this is homepage')
    aboutdata=about.objects.get(id=1)
    clientData=clientsModel.objects.all()
    context={
        'about':aboutdata,
        'clients':clientData,
    }
    return render (request,'index.html',context)

def services (request):
    return render (request,'services.html')

def portfolio (request):
    return render (request,'portfolio.html')


def pricing (request):
    productData=pricingModel.objects.get(id=1)
    prods={
        'product':productData
    }
    return render (request,'pricing.html', prods)


def contact (request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contactformdata=contactform(name=name, email=email, subject=subject, message=message)
        contactformdata.save()

    return render (request,'contact.html')