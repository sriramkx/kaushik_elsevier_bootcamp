from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2(request):
    return HttpResponse('this is app2 page')

def login(request):
    return('this is login page')
