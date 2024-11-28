from django import forms
from .models import User, UserType
from django.contrib.auth.forms import AuthenticationForm

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")  # Para ocultar la contraseña al escribir

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'middle_name', 'phone', 'user_type', 'password']
        widgets = {
            'user_type': forms.Select(attrs={'class': 'form-control'}),
        }

class UserTypeForm(forms.ModelForm):
    class Meta:
        model = UserType
        fields = ['name', 'description']

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, label="Nombre de usuario")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    
    class Meta:
        model = User
        fields = ['username', 'password']