from django.shortcuts import render
from .models import Plat

def plats(request):
    plats = Plat.objects.all()
    return render(request, 'gestion_menus_plats/plats.html', {'plats': plats})
