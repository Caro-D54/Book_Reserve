from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LibroViewSet, SucursalViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'libros', LibroViewSet)
router.register(r'sucursales', SucursalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]