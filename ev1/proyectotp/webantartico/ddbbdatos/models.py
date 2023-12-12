from django.db import models
import sqlite3

# Create your models here.
class Persona(models.Model):
    IdPersona=models.IntegerField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    IdTelefono = models.IntegerField(Telefono, on_delete=models.CASCADE)
    
    class Telefono(models.Model):
        IdTelefono = models.IntegerField()
        telefono = models.CharField(max_length=15)
        codigoArea = models.CharField(max_length=10)
        
       
   