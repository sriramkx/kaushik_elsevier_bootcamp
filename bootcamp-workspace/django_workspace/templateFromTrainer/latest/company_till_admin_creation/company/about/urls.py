
from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.about),
    path('team/',views.team),
    path('testimonial/',views.testimonial),
    
]
