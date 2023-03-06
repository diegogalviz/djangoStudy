from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulo
from django.conf import settings
from django.core.mail import send_mail
from gestionPedidos.forms import FormularioContacto


# Create your views here.

def busqueda_articulo(request):
    return render(request, 'busqueda_articulo.html')


def buscar(request):
    if request.GET['Articulo']:
        # mensaje = f'Articulo buscado: {request.GET["Articulo"]} '
        producto = request.GET['Articulo']

        if len(producto) > 20:
            mensaje = 'el nombre es demaciado largo'

        else:
            articulos = Articulo.objects.filter(nombre__icontains=producto)
            print(producto)

            ctx = {'articulos': articulos, 'query': producto}

            return render(request, 'resultados_busqueda.html', ctx)

    else:
        mensaje = ' no has introducido nada'

    return HttpResponse(mensaje)


def contacto(request):
    if request.method == 'POST':

        miFormulario = FormularioContacto(request.POST)

        if miFormulario.is_valid():
            infForm = miFormulario.cleaned_data
            send_mail(infForm['asunto'], infForm['mensaje'], infForm.get('email', ' '), ['arqdiegogalvizv@gmail.com'])
            return HttpResponse('gracias por enviar su mensaje')
    else:
        miFormulario = FormularioContacto()

    ctx = {'form': miFormulario}
    return render(request, 'formulario_contacto.html', ctx)

    # if request.method == 'POST':
    #     subject = request.POST['asunto']
    #     message = request.POST['mensaje'] + " " + request.POST['email']
    #     email_from = settings.EMAIL_HOST_USER
    #     recipient_list=['arqdiegogalvizv@gmail.com']
    #     send_mail(subject, message, email_from, recipient_list, fail_silently=False)
    #     return HttpResponse('gracias por enviar su mensaje')
    # return render(request, 'contacto.html')
