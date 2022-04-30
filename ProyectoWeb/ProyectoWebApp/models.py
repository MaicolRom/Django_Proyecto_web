from multiprocessing.sharedctypes import Value
from django.db import models

class Persona(models.Model):
    nombre=models.CharField(max_length=100)
<<<<<<< HEAD
    cedula=models.IntegerField(max_length=100)
    archivo=models.FileField(upload_to='archivos/documentos/')
=======
    cedula=models.IntegerField(blank=True )
    archivo=models.FileField(upload_to='archivos/documentos/', blank=True)

>>>>>>> c2fb4a25b8909e780c2740b6ad619bea7422a03d

    def __str__(self):
        return self.title
