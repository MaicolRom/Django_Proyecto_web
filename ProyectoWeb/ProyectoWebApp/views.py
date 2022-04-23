from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import personaForm
from django.http import HttpResponse
import os

# Create your views here.
def home(request):
    return render(request, 'ProyectoWebApp/upload.html')

def upload(request):
    context={}
    if request.method =='POST':
        uploaded_file=request.FILES['Documento']
        fs = FileSystemStorage()
        name=fs.save(uploaded_file.name, uploaded_file)
        context['url']=fs.url(name)

    return render(request, 'ProyectoWebApp/upload.html', context)

def lista_personas(request):
    return render(request, 'ProyectoWebApp/lista_personas.html')

def carga_personas(request):
    form=personaForm()
    return render(request, 'ProyectoWebApp/carga_personas.html', {'form': form})

def create_folder(request):
    return render(request, "create_folders.html")

def folder(request):
    if request.GET['folder_name']:
        folder=request.GET['folder_name']
        route='D:/Projectos_Django/'
        os.mkdir(route+folder)
        os.mkdir(route+folder+'/doc1')
        os.mkdir(route+folder+'/doc2')
        os.mkdir(route+folder+'/doc3')
        os.mkdir(route+folder+'/doc4')
        mensaje='usuario creado'
    else:
        mensaje='No has introducido usuario a crear'
    return HttpResponse(mensaje)

def validation_folder(request):
    a=os.listdir('D:\Projectos_Django\maicol romero')
    b=os.listdir('D:\Projectos_Django\maicol romero\doc2')

    if len(b) > 0:
        print('True')
    else:
        print('False')