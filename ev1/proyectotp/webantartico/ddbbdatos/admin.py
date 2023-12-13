from django.contrib import admin
from .models import Persona

# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('IdPersona', 'nombre', 'apellido', 'correo', 'telefono')

admin.site.register(Persona, PersonaAdmin)
