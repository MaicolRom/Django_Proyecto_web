from multiprocessing.sharedctypes import Value
from django.db import models

class Persona(models.Model):
    nombre=models.CharField(max_length=100)
    cedula=models.IntegerField(blank=True )
    archivo=models.FileField(upload_to='archivos/documentos/', blank=True)



    def __str__(self):
        return self.title
