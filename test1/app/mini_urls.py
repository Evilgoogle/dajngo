from django.urls import path, re_path, include
from app import views

urlpatterns = [
    path('contact', views.contact),
]