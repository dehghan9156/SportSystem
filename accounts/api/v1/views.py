from http.client import responses
from django.conf import settings
from django.core.serializers import serialize
from django.db.models.fields import return_None
from django.shortcuts import get_object_or_404
from django.template.context_processors import request
from rest_framework import generics,viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.generics import CreateAPIView,GenericAPIView
from .serialization import *
from .permissions import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


from django.contrib.auth import get_user_model
User = get_user_model()



class UserRegisterApiView(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            username = serializer.validated_data["username"]
            return Response({"message":f"{username} register successfully"},status=status.HTTP_200_OK)
        return Response(serializer.errors)

class UserLoginApiView(generics.GenericAPIView):
    serializer_class=UserLoginSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = authenticate(request,username=serializer.validated_data["username"],password=serializer.validated_data["password"])
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'username':user.username,
                    'role':user.role,
                })
            return Response({"message":"username or password not correct"})
        return Response(serializer.errors)
