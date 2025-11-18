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
    permission_classes = [IsAdminUser]  # Solo admin puede gestionar libros


# --- CRUD de Sucursales ---
class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer
    permission_classes = [IsAdminUser]  # Solo admin puede gestionar sucursales


# --- CRUD de Solicitudes ---
class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsAdminUser]  # Solo admin puede aprobar/rechazar solicitudes

    # Acción personalizada: aprobar solicitud
    @action(detail=True, methods=["patch"], permission_classes=[IsAdminUser])
    def approve(self, request, pk=None):
        req = self.get_object()
        req.status = "aprobada"
        req.save()
        return Response({"message": "Solicitud aprobada"}, status=status.HTTP_200_OK)

    # Acción personalizada: rechazar solicitud
    @action(detail=True, methods=["patch"], permission_classes=[IsAdminUser])
    def reject(self, request, pk=None):
        req = self.get_object()
        req.status = "rechazada"
        req.save()
        return Response({"message": "Solicitud rechazada"}, status=status.HTTP_200_OK)

    # Permitir actualización directa del campo status con PATCH
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        status_value = request.data.get("status")
        if status_value:
            instance.status = status_value
            instance.save()
            return Response({"message": f"Solicitud {status_value}"}, status=status.HTTP_200_OK)
        return super().partial_update(request, *args, **kwargs)
