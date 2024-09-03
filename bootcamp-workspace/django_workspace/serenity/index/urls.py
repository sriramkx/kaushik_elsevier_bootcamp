
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.index, name='home'),
    path('services/',views.services, name='services'),
    path('portfolio/',views.portfolio, name='portfolio'),
    path('pricing/',views.pricing, name='pricing'),
    path('blog/',views.blog, name='blog'),
    path('contact/',views.contact, name='contact'),
   
]
