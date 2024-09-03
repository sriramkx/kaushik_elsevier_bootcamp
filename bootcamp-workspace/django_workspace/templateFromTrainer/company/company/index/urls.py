
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.home),
    path('services/',views.services),
    path('portfolio/',views.portfolio),
    path('pricing/',views.pricing),
    path('contact/',views.contact),
   
]
