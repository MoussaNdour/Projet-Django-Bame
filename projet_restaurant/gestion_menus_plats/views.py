from django.shortcuts import render
from .models import Plat

def plats(request):
    plats = Plat.objects.all()
    categories = [
        ('entree', 'Entrées'),
        ('plat_resistant', 'Plats Résistants'),
        ('dessert', 'Desserts'),
    ]
    return render(request, 'gestion_menus_plats/plats.html', {'plats': plats,'categories':categories})
