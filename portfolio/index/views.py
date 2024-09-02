from django.shortcuts import render
from django.http import HttpResponse
from .models import about
from .models import slider
from .models import client



def aboutus(request):
    return render(request,'about.html')



def home(request):
    aboutdata = about.objects.all()[0]
    sliderdata = slider.objects.all()
    clientdata = client.objects.all()
    
    context = {
        'about': aboutdata,
        'slider': sliderdata,
        'client':clientdata
       
    }
    return render(request,'index.html',context)








def service(request):
    return render(request,'service.html')

def blog(request):
    return render(request,'blog.html')


def pricing(request):
    return render(request,'pricing.html')




def data(request):
    data='data from database'
    return HttpResponse(data)