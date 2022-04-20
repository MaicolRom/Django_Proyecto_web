from django.db import models

class Persona(models.Model):
    nombre=models.CharField(max_length=100)
    cedula=models.IntegerField(max_length=100)
    archivo=models.FileField(upload_to='archivos/documentos/')

    def __str__(self):
        return self.title
