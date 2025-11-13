from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  LibroViewSet, SucursalViewSet

router = DefaultRouter()

router.register(r'libros', LibroViewSet, basename='libro')
router.register(r'sucursales', SucursalViewSet, basename='sucursal')

urlpatterns = [
    path('', include(router.urls)),
]