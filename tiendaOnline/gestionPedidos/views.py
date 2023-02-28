from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulo


# Create your views here.

def busqueda_articulo(request):
    return render(request, 'busqueda_articulo.html')


def buscar(request):
    if request.GET['Articulo']:
        # mensaje = f'Articulo buscado: {request.GET["Articulo"]} '
        producto = request.GET['Articulo']
        articulos = Articulo.objects.filter(nombre__icontains=producto)

        ctx = {'articulos': articulos, 'query': producto}

        return render(request, 'resultados_busqueda.html', ctx)

    else:
        mensaje = ' no has introducido nada'

    return HttpResponse(mensaje)
