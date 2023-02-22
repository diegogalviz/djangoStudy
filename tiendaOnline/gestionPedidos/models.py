from django.db import models


# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    tel = models.CharField(max_length=10)


class Articulo(models.Model):
    nombre = models.CharField(max_length=50)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return f'el nombre del articulo es: {self.nombre}, la seccion del articulo es:{self.seccion}, el precio del articulo es{self.precio}'


class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entrgado = models.BooleanField()
