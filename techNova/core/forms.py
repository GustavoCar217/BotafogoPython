from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Nome de Usuário", 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="Senha", 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
