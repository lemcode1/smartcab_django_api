from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User

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
class loginDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def post(self,request,*args,**kwargs):
 #   print(request.data.username)
    print(request.data)
    print(type(request.data))
    print(request.data["Username"])
    user = User.objects.get(Username=request.data["Username"],password=request.data["password"])

    serializer = UserSerializer(user)
    return Response(serializer.data)




