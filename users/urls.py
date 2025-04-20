"""Defines URL pattens for users"""

from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # Include the default auth urls
    path('', include('django.contrib.auth.urls')),
    # Include the user registration urls
    path('register/', views.register, name='register'),
]