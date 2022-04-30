from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import personaForm

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