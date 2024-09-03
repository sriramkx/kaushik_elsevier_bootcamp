from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def about(request):
    return render (request,'about/about.html')

def team (request):
    return render (request,'about/team.html')

def testimonial (request):
    return render (request,'about/testimonial.html')