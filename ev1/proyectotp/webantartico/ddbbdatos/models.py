from django.db import models
import mysql.connector

conexion = mysql.connector.connect(user='root', 
                                   password='1234', 
                                   host='localhost', 
                                   database='contact', 
                                   port = '3306')

print(conexion)
# import sqlite3
# Create your models here.
# class Persona(models.Model):
#     IdPersona=models.IntegerField()
#     nombre = models.CharField(max_length=50)
#     apellido = models.CharField(max_length=50)
#     correo = models.CharField(max_length=50)
#     IdTelefono = models.IntegerField()
    
#     class Telefono(models.Model):
#         IdTelefono = models.IntegerField()
#         telefono = models.CharField(max_length=15)
#         codigoArea = models.CharField(max_length=10)
        
       
   