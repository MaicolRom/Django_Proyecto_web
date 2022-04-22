from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import personaForm
from .models import Persona

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
    persona=Persona.objects.all()
    return render(request, 'ProyectoWebApp/lista_personas.html', {
        'persona':persona
    })

def carga_personas(request):
    if request.method == 'POST':
        form=personaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_personas')
    else:
        form=personaForm
    return render(request, 'ProyectoWebApp/carga_personas.html', {'form': form})