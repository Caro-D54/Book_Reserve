from django.test import TestCase
from .models import Libro, Sucursal


class LibroModelTest(TestCase):
    def test_crear_libro(self):
        libro = Libro.objects.create(
            titulo="Cien años de soledad",
            autor="Gabriel García Márquez",
            fecha_publication="1967-05-30",
            descripcion="Novela emblemática del realismo mágico",
            genero="Novela",
            cantidad_paginas=417,
            idioma="Español",
            precio_prestamo_fisico=12.50
        )
        # Verificamos que se creó correctamente
        self.assertEqual(libro.titulo, "Cien años de soledad")
        self.assertEqual(str(libro), "Cien años de soledad")


class SucursalModelTest(TestCase):
    def test_crear_sucursal(self):
        sucursal = Sucursal.objects.create(
            nombre="Sucursal Centro",
            direccion="Calle Mayor 123",
            telefono="123456789",
            correo="centro@example.com",
            prestamos_fisicos=100.00,
            prestamos_digitales=50.00
        )
        # Verificamos que se creó correctamente
        self.assertEqual(sucursal.nombre, "Sucursal Centro")
        self.assertEqual(str(sucursal), "Sucursal Centro")