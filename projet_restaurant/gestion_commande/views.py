from django.shortcuts import render, redirect
from .models import Commande, LigneCommande
from .forms import LigneCommandeForm

def passer_commande(request):
    if request.method == 'POST':
        form = LigneCommandeForm(request.POST)
        if form.is_valid():
            commande = Commande.objects.create(client=request.user)
            ligne = form.save(commit=False)
            ligne.commande = commande
            ligne.save()
            return redirect('accueil:index')
    else:
        form = LigneCommandeForm()
    
    return render(request, 'gestion_commandes/commander.html', {'form': form})
