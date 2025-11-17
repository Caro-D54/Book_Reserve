# Book_Reserve/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_root(_request):
    return JsonResponse({
        "mensaje": "Bienvenido a la API de Librería de Nexus Literario",
        "endpoints": [
            "/api/users/register/",
            "/api/users/token/",
            "/api/users/token/refresh/",
            "/api/users/me/",
            "/api/users/logout/",
            "/api/library/libros/",
            "/api/library/sucursales/",
        ]
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root),

    # Rutas de la app Library
    path('api/library/', include('Library.urls')),

    # Rutas de la app Users_management (autenticación con JWT)
    path('api/users/', include('Users_management.urls')),
]
