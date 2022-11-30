from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome_view(request):
    return HttpResponse("<h2 style='color:red'>let's start the work<h2/>")



from rest_framework.permissions import AllowAny
from .serializers import UserSerializer,UserSerializer
from rest_framework import generics

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = UserSerializer




