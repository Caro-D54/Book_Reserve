from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import  Libro, Sucursal
from .serializer import UserSerializer, LibroSerializer, SucursalSerializer



class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer