from django.shortcuts import render
from django.http import HttpResponse
from .models import newsmodel
from .models import postFeed

def index(request):
    newsdata = newsmodel.objects.get(id=1)
    context = {
        'newsdata' : newsdata
    }

    if request.method == 'POST':
        postContent = request.POST.get('postForm')
        # imageUploaded = request.POST.get('uploadedPhoto')
        postFeedData = postFeed(postContent=postContent)
        postFeedData.save()

    return render (request,'index.html',context)