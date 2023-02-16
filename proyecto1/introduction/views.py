import datetime
from django.http import HttpResponse
from django.template import Template, Context


class Persona(object):
    def __int__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def saludo(request):  # primera vista
    nombre = 'Diego '
    apellido = 'Galviz Velandia'
    # per = Persona( nombre , apellido )
    ahora = datetime.datetime.now()
    doc_externo = open(r'C:\Users\ING ANNETH LUNA ROZO\Desktop\djangoStudy\proyecto1\plantillas\plantilla1.html')
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({'nombre_persona': nombre, 'apellido_persona': apellido, 'ahora': ahora})

    documento = plt.render(ctx)
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
    periodo = year - 2023
    edadFutura = edad + periodo

    documento = f'<html><body><h2> En el año {year} tendras {edadFutura} </h2></body></html>'

    return HttpResponse(documento)
