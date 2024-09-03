from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    return render(request,'about/about.html')
    #return HttpResponse('this is about page')

def team(request):
    return render(request,'about/team.html')
    #return HttpResponse('this is team page')

def testimonial(request):
    return render(request,'about/testimonial.html')
    #return HttpResponse('this is testimonial page')