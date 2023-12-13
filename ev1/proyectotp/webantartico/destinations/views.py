from django.shortcuts import render
from .models import Flip_card

# Create your views here.
def destinations(request):
    Flip_cards = Flip_card.objects.all()
    return render(request, "destinations/destinations.html", {'Flip_cards':Flip_cards})