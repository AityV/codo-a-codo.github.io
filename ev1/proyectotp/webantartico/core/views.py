from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "core/base.html")

# def destinations(request):
#     return render(request, "core/destinations.html")

def packages(request):
    return render(request, "core/packages.html")

def construction(request):
    return render(request, "core/construction.html")