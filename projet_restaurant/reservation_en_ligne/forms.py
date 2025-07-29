from django import forms
from .models import Reservation, Table

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table']
        widgets = {
            'table': forms.Select(attrs={'class': 'form-select'}),
        }
