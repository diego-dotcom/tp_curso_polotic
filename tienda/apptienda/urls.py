from django.urls import path
from . import views

app_name ="apptienda"
urlpatterns = [
    path('', views.index, name="index"),
    path('acerca', views.acerca, name="acerca"),
    path('<int:producto_id>', views.producto, name="producto"),
    path('producto_alta', views.producto_alta, name="producto_alta"),
    path('producto_editar/<int:producto_id>', views.producto_editar, name="producto_editar"),
    path('producto_eliminar/<int:producto_id>', views.producto_eliminar, name="producto_eliminar"),
    path('filtro_categorias/<int:categoria_id>', views.filtro_categorias, name="filtro_categorias"),
    path('filtro_texto', views.filtro_texto, name="filtro_texto"),
    path('registro', views.registro, name="registro"),
    path('carrito', views.carrito, name="carrito"),
]
