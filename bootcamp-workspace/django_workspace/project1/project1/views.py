from django.http import HttpResponse

def home(request):
    return HttpResponse('this is homepage')

def about(request):
    return HttpResponse('this is aboutpage')

def service(request):
    return HttpResponse('this is servicepage')

def contact(request):
    return HttpResponse('this is contactpage')