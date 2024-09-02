
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee),
    path('profile/', views.profile,name='profile'),
    path('new/', views.new),
    
]
