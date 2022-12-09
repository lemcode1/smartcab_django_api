from django.contrib import admin
from django.urls import path
from . import views
from .views import RegisterUserAPIView, loginDetailAPI

urlpatterns = [
    path('welcome/', views.welcome_view),
    path('RegisterUser/',RegisterUserAPIView.as_view()),
    path('api/login-detail/',loginDetailAPI.as_view())
]





