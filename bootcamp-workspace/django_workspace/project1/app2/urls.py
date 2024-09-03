from django.urls import path
from . import views
urlpatterns = [
    path('', views.app2),
    path('login/', views.login)
]