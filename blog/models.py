from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

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
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.cliente} - {self.producto} (x{self.cantidad})"
    
class Post(models.Model):

    titulo = models.CharField(max_length=100)

    subtitulo = models.CharField(max_length=200)

    contenido = RichTextField()

    imagen = models.ImageField(upload_to='posts', null=True, blank=True)

    fecha = models.DateField()

    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    


