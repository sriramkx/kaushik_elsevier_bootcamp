from django.http import HttpResponse

def home(request):
    return HttpResponse('this is home page')

def about(request):
    return HttpResponse('this is about page')

def services(request):
    return HttpResponse('this is services page')

def portfolio(request):
    return HttpResponse('this is portfolio page')

def pricing(request):
    return HttpResponse('this is pricing page')

def blog(request):
    return HttpResponse('this is blog page')

def contact(request):
    return HttpResponse('this is contact page')