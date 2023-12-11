from django.db import models

# Create your models here.
class Persona(models.Model):
    IdPersona=models.IntegerField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    IdTelefono = models.IntegerField()
    
    class Telefono(models.Model):
        IdTelefono = models.IntegerField()
        telefono = models.CharField(max_length=15)
        codigoArea = models.CharField(max_length=10)
        
       
   