from django.urls import path
from . import views
urlpatterns = [
    path('', views.app1),
    path('faq/', views.faq)
]
