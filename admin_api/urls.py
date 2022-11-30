from django.contrib import admin
from django.urls import path
from . import views
from .views import RegisterUserAPIView
urlpatterns = [
    path('welcome/', views.welcome_view),
    path('RegisterUser/',RegisterUserAPIView.as_view())
]