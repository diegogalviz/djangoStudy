import datetime

from django.http import HttpResponse


def saludo(request):  # primera vista
    documento = '''
    <html>
    <body>
    <h1> Hola diego otra vez <h1>
    <body>
    <html>'''
    return HttpResponse(documento)


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
    periodo = year-2023
    edadFutura = edad + periodo

    documento = f'<html><body><h2> En el año {year} tendras {edadFutura} </h2></body></html>'

    return HttpResponse(documento)
