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
from rest_framework import viewsets
from ...models import *
from .serialization import *
from accounts.api.v1.permissions import *

from django.contrib.auth import get_user_model
User = get_user_model()

class CategoryApiViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class RaceApiViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = RaceSerializer
    queryset = Race.objects.all()

class ManagerRaceListCreateApiView(generics.ListCreateAPIView):
    permission_classes = [IsRaceManager]
    serializer_class = RaceSerializer
    queryset = Race.objects.all()

    def get_queryset(self):
        race = Race.objects.filter(race_manager=self.request.user)
        return race

class ManagerRaceRetrieveUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes =[IsRaceManager]
    serializer_class = RaceSerializer
    queryset  = Race.objects.all()

    def get_queryset(self):
        race = Race.objects.filter(user_manager=self.request.user)
        return race