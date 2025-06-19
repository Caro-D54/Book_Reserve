from django.db import models


# Create your models here.




class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    fecha_publication = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    genero = models.CharField(max_length=100)
    cantidad_paginas = models.IntegerField()
    idioma = models.CharField(max_length=100)
    precio_prestamo_fisico = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.titulo

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField(unique=True)
    prestamos_fisicos = models.DecimalField(max_digits=10, decimal_places=2)
    prestamos_digitales = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
