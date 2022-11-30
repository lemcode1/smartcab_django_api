from .views import RegisterAPI
from django.urls import path

urlpatterns = [
    path('api/register_user/', RegisterAPI.as_view(), name='register'),
]