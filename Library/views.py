# Library/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from .models import Libro, Sucursal, Request
from .serializer import LibroSerializer, SucursalSerializer, RequestSerializer


# --- CRUD de Libros ---
class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


# --- CRUD de Sucursales ---
class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer


# --- CRUD de Solicitudes con acciones personalizadas ---
class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    # Acción personalizada: aprobar solicitud
    @action(detail=True, methods=["post"], permission_classes=[IsAdminUser])
    def approve(self, request, pk=None):
        req = self.get_object()
        req.status = "Aprobada"
        req.save()
        return Response({"message": "Solicitud aprobada"}, status=status.HTTP_200_OK)

    # Acción personalizada: rechazar solicitud
    @action(detail=True, methods=["post"], permission_classes=[IsAdminUser])
    def reject(self, request, pk=None):
        req = self.get_object()
        req.status = "Rechazada"
        req.save()
        return Response({"message": "Solicitud rechazada"}, status=status.HTTP_200_OK)
