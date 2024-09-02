from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def employee(request):
    return render(request,'employee/employee.html')
  
  


def profile(request):
    return render(request,'employee/profile.html')


def new(request):
    return HttpResponse('this is new page')




