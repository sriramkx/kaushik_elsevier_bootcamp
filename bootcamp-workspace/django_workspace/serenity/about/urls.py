from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial')    
]
