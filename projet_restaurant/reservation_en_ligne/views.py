from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Table
from django.contrib.auth.decorators import login_required

@login_required
def reserver(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.client = request.user
            table = reservation.table
            if table.disponible:
                reservation.save()
                table.disponible = False
                table.save()
                return render(request, 'reservation_en_ligne/confirmation.html', {'reservation': reservation})
            else:
                form.add_error('table', "Cette table n’est plus disponible.")
    else:
        form = ReservationForm()
    return render(request, 'reservation_en_ligne/reserver.html', {'form': form})
