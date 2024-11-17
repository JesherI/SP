from django import forms
from .models import User, UserType

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