from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'username': '',
            'password1': '',
            'password2': '',
        }

       

class CustomAuthenticationForm(AuthenticationForm):
     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
