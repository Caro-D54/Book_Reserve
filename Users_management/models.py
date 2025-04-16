from django.db import models

# Create your models here.
class User(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contrasena = models. CharField(max_length=255)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255)
    fecha_devolucion = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre