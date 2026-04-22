from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    cliente = models.CharField(max_length=50)
    producto = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.cliente} - {self.producto}"


