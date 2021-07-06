from django.shortcuts import render, redirect
from .carro import Carro
from apptienda.models import Producto
from django.contrib import messages

# Create your views here.

def agregar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("apptienda:carrito")

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("apptienda:carrito")

def restar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("apptienda:carrito")

def limpiar_carro(request):
    carro=Carro(request)
    carro.limpiar_carro()
    messages.info(request, 'Su carrito ha quedado vacío')
    return redirect("apptienda:index")