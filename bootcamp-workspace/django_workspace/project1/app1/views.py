from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def app1(request):
    return HttpResponse('this is app1 page')

def faq(request):
    return HttpResponse('this is faq page')

