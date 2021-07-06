from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    descripcion = models.CharField(max_length=64)

    def __str__(self):
        return f"Categoría {self.descripcion}"


class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="categoria")
    titulo = models.CharField(max_length=64, null=False)
    imagen = models.FileField(upload_to='img_productos/', blank= True)
    descripcion = models.TextField(default= '', null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default = 0.00)
    fecha_publicacion = models.DateField(null= False)
  

    def __str__(self):
        return f"{self.titulo} ({self.categoria}): ${self.precio}. Publicado {self.fecha_publicacion}"


class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Usuario')
    productos = models.ManyToManyField(Producto)
    total = models.DecimalField(max_digits=10, decimal_places=2, default = 0.00)

    def __str__(self):
        return f'{self.usuario} tienes un carrito de $ {self.total} con los siguientes productos: {self.productos}'
