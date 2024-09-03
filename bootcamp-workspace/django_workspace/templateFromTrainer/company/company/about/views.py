from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def about(request):
    return render(request, 'about/about.html')
    #return HttpResponse('this is aboutpage')

def team (request):
    return render(request, 'about/team.html')
    #return HttpResponse('this is team ')

def testimonial (request):
    return render(request, 'about/testimonial.html')
    #return HttpResponse('this is testimonial ')