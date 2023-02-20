import datetime
from django.http import HttpResponse
# from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def saludo(request):  # primera vista
    temas = ['React', 'Django', 'PostgreSQL']

    nombre = 'Salomé '
    apellido = 'Galviz Velandia'
    per = Persona(nombre, apellido)
    ahora = datetime.datetime.now()
    # doc_externo = open(r'C:\Users\ING ANNETH LUNA ROZO\Desktop\djangoStudy\proyecto1\templates\plantilla1.html')
    # plt = Template(doc_externo.read())
    # doc_externo.close()
    # doc_externo = get_template('plantilla1.html')
    # ctx = Context({'nombre_persona': per.nombre, 'apellido_persona': per.apellido, 'ahora': ahora, 'temas': temas})
    # documento = doc_externo.render(ctx)
    # return HttpResponse(documento)
    ctx = {'nombre_persona': per.nombre, 'apellido_persona': per.apellido, 'ahora': ahora, 'temas': temas}
    return render(request, 'plantilla1.html', ctx)


def despedida(request):
    return HttpResponse('hasta luego alumnos')


def dameFecha(request):
    fecha_actual = datetime.datetime.now()

    documento = '''
        <html>
        <body>
        <h2>
         Fecha y hora actuales %s
        </h2>
        </body>
        </html>
        ''' % fecha_actual
    return HttpResponse(documento)


def calculaEdad(request, edad, year):
    periodo = year - 2023
    edadFutura = edad + periodo

    documento = f'<html><body><h2> En el año {year} tendras {edadFutura} </h2></body></html>'

    return HttpResponse(documento)


def home(request):
    return HttpResponse('este es el home')

def curso(request):
    fecha_actual = datetime.datetime.now()
    ctx= {'dameFecha': fecha_actual}
    return render(request, 'cursoC.html',ctx)
