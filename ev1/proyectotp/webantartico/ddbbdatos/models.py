from django.db import models

# Create your models here.

class Persona(models.Model):
    IdPersona=models.IntegerField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)

    class Meta:
        ordering = ['IdPersona']