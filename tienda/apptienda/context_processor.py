from .models import Categoria   

def categorias(request):
    lista_categorias = Categoria.objects.all()
    return {'lista_categorias': lista_categorias}


def grupos(request):
    es_usuario = request.user.groups.filter(name='Usuarios').exists()
    es_moderador = request.user.groups.filter(name='Moderadores').exists()
    return {
        'es_usuario': es_usuario,
        'es_moderador': es_moderador,
    }