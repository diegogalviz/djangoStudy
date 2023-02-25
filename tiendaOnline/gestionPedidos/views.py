from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def busqueda_articulo(request):
    return render(request, 'busqueda_articulo.html')
def buscar(request):
    mensaje = f'Articulo buscado: {request.GET["Articulo"]} '
    return HttpResponse(mensaje)
