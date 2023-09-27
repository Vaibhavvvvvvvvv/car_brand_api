from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics

class listcar(generics.ListCreateAPIView):
    queryset=Carmodel.objects.all()
    serializer_class=carserilizers

class rld(generics.RetrieveUpdateDestroyAPIView):
    queryset=Carmodel.objects.all()
    serializer_class=carserilizers