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
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))