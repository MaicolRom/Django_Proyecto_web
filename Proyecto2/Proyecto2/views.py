from contextvars import Context
from datetime import datetime
from pipes import Template
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
#Primera vista

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def Saludo(request):
    P1=Persona("Maicol Se", "Romero Buitrago")
    temas=["Plantillas","Modelos","Formularios","Vistas","Despliegue"]
    fecha_actual=datetime.datetime.now()
    #doc_externo=open("C:/Users/maico/AppData/Local/Programs/Python/Python310/DJANGO_ENV/Proyecto2/Proyecto2/Plantillas/1Plantilla.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    #doc_externo=get_template('1Plantilla.html')
    #ctx=Context()
    #documento=doc_externo.render({"nombre_persona": P1.nombre, "apellido_persona":P1.apellido, "ahora":fecha_actual, "Temas":temas})
    return render(request, "1Plantilla.html",{"nombre_persona": P1.nombre, "apellido_persona":P1.apellido, "ahora":fecha_actual, "Temas":temas})

def herencia(request):
    fecha_actual=datetime.datetime.now()
    return render(request, "Herencia.html", {"dameFecha":fecha_actual})

def Despedida(request):
    return HttpResponse("Chao Mundo")

def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html>
    <body>
    <h1>
    Fecha y hora %s
    </h1>
    </body>
    </html>
    """% fecha_actual

    return HttpResponse(documento)

def calcularEdad(request, edad, anio):
    periodo=anio-2022
    edadFutura=edad+periodo
    documento="<html><body><h1>Es el año %s tendrás %s años</h1></body></html>"%(anio, edadFutura)
    return HttpResponse(documento)
