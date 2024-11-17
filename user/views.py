from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm, UserTypeForm
from .models import User, UserType

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # No guardar aún
            user.set_password(form.cleaned_data['password'])  # Encriptar la contraseña
            user.save()  # Ahora guardar
            messages.success(request, f"Usuario {user.username} creado exitosamente.")
            return redirect('user_list')  # Cambiar por la vista/lista de usuarios que prefieras
    else:
        form = UserForm()
    
    return render(request, 'add_user.html', {'form': form})


def add_user_type(request):
    if request.method == 'POST':
        form = UserTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Tipo de usuario '{form.cleaned_data['name']}' creado exitosamente.")
            return redirect('list_user_types')  # Cambia esto según tu flujo de navegación
    else:
        form = UserTypeForm()
    
    return render(request, 'add_user_type.html', {'form': form})

def list_user_types(request):
    user_types = UserType.objects.all()
    return render(request, 'list_user_types.html', {'user_types': user_types})