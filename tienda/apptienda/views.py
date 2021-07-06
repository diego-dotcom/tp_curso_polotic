from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .forms import *
from .models import Categoria, Producto
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.

def index(request):

    return render(request,"apptienda/index.html", {
        "lista_productos": Producto.objects.all(),
        "productos_card": Producto.objects.all().order_by('-id')[:3],
        "productos_resto": Producto.objects.all().order_by('-id')[3:10],
    })

def acerca(request):
    return render(request, "apptienda/acercade.html")

def producto(request, producto_id):
    un_producto = get_object_or_404(Producto, id=producto_id)
    return render(request, "apptienda/producto.html", {
        "producto": un_producto,
    })

@login_required
def producto_alta(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user)
        form = FormProducto(request.POST, request.FILES)      
        if form.is_valid():
            form.save()
            messages.success(request, f'Producto agregado con éxito')
            return redirect("apptienda:index")          
    else:
        form = FormProducto(initial={'fecha_publicacion':timezone.now()})
        return render(request, "apptienda/producto_nuevo.html", {
            "form": form,
        })

@login_required
def producto_editar(request, producto_id):
    un_producto = get_object_or_404(Producto, id=producto_id)
    if request.method == "POST":  
        user = User.objects.get(username=request.user)   
        un_producto.editor = user
        form = FormProducto(data=request.POST, files=request.FILES, instance=un_producto)
        if form.is_valid():
            form.save()
            messages.success(request, f'Producto modificado con éxito')
            return redirect("apptienda:index")
    else:
        form = FormProducto(instance = un_producto)
        return render(request, 'apptienda/producto_editar.html', {
            "producto": un_producto,
            "form": form
        })

@login_required
def producto_eliminar(request, producto_id):
    un_producto = get_object_or_404(Producto, id=producto_id)
    un_producto.delete()
    messages.success(request, f'Producto eliminado con éxito')
    return redirect("apptienda:index")


def filtro_categorias(request, categoria_id):
    una_categoria = get_object_or_404(Categoria, id=categoria_id)
    queryset = Producto.objects.all()
    queryset = queryset.filter(categoria=una_categoria)
    return render(request,"apptienda/busqueda_cat.html", {
        "lista_productos": queryset,
        "categoria_seleccionada": una_categoria
    })


def filtro_texto(request):
    texto = request.POST.get('texto', '')
    queryset = Producto.objects.all()
    lista = queryset.filter(
        Q(titulo__contains=texto) |
        Q(descripcion__contains=texto)
    )
    return render(request,"apptienda/busqueda_texto.html", {
        "lista_productos": lista,
        "texto": texto,
    })


def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado con éxito')
            return redirect("apptienda:index")
    else:
        form = UserRegisterForm()
    context = { 'form': form } 
    return render(request, 'apptienda/registro.html', context)


def carrito(request):
    return render(request, "apptienda/carrito.html")