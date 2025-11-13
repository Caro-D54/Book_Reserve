from django.contrib import admin
from .models import Libro, Sucursal

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "genero", "idioma", "precio_prestamo_fisico")
    search_fields = ("titulo", "autor", "genero")

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "telefono", "correo")
    search_fields = ("nombre", "direccion", "correo")