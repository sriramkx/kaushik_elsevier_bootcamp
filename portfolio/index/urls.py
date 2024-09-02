from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.aboutus,name='about'),
    path('', views.home,name='home'),
    path('service/', views.service,name="service"),
    path('pricing/', views.pricing,name="pricing"),
    path('blog/', views.blog,name="blog"),
    path('data/', views.data),
    
]
