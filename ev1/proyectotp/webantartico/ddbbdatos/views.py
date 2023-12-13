from django.shortcuts import render, redirect
from .models import Persona
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.

def contact(request):
    personas = Persona.objects.all()
    message = request.GET.get('message', None)
    return render(request, "ddbbdatos/contact.html", {'persona': personas, 'message': message})

def process_form(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        tel = request.POST.get('tel')

        # Crear una nueva instancia de Persona y guardar en la base de datos
        persona = Persona(nombre=firstname, apellido=surname, correo=email, telefono=tel)
        persona.save()

        message = "¡Datos guardados correctamente!"
        
        return redirect(f'/contact/?message={message}')

    return HttpResponse("Error: Se esperaba una solicitud POST.")

