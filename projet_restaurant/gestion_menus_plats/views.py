from django.shortcuts import render,redirect
from .models import Plat
from .forms import PlatForm

def plats(request):
    plats = Plat.objects.all()
    categories = [
        ('entree', 'Entrées'),
        ('plat_resistant', 'Plats Résistants'),
        ('dessert', 'Desserts'),
    ]
    return render(request, 'gestion_menus_plats/plats.html', {'plats': plats,'categories':categories})

def ajouter_plat(request):
    if request.method == 'POST':
        form = PlatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('nom_de_ta_vue_de_liste')  # adapte selon ton projet
    else:
        form = PlatForm()
    return render(request, 'gestion_menus_plats/ajouter.html', {'form': form})