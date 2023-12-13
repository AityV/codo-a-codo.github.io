from django.shortcuts import render
from .models import Persona

# Create your views here.

def contact(request):
    personas = Persona.objects.all()
    return render(request, "ddbbdatos/contact.html", {'persona': personas})

