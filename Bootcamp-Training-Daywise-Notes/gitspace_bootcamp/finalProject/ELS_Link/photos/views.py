from django.shortcuts import render
from .models import photo

# Create your views here.
from django.http import HttpResponse

def photos(request):
    photodata = photo.objects.all()
    context={
        'photo': photodata
    }
    return render (request,'photos/photos.html',context)