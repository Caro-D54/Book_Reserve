from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  LibroViewSet, SucursalViewSet, RequestViewSet

router = DefaultRouter()

router.register(r'libros', LibroViewSet)
router.register(r'sucursales', SucursalViewSet)
router.register(r'solicitudes', RequestViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]