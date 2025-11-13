from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework.authtoken.views import obtain_auth_token

def api_root(_request):
    return JsonResponse({
        "mensaje": "Bienvenido a la API de Libreria de Nexus Literario", "endpoints": [
        "/api/users/token/",
        "/api/users/token/refresh/",
        "/api/users/protected/",
        "/api/library/libros/",
        "/api/library/sucursales/",
    ]})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root),
    
    path('api/library/', include('Library.urls')),
    path('api/users/', include('Users_management.urls')),
    path('api-token-auth/', obtain_auth_token),
]