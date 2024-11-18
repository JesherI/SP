from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm, UserTypeForm, CustomLoginForm
from django.contrib.auth import login, authenticate
from .models import User, UserType

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) 
            user.set_password(form.cleaned_data['password']) 
            user.save() 
            messages.success(request, f"Usuario {user.username} creado exitosamente.")
            return redirect('user_list') 
    else:
        form = UserForm()
    
    return render(request, 'add_user.html', {'form': form})

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


def add_user_type(request):
    if request.method == 'POST':
        form = UserTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Tipo de usuario '{form.cleaned_data['name']}' creado exitosamente.")
            return redirect('list_user_types')
    else:
        form = UserTypeForm()
    
    return render(request, 'add_user_type.html', {'form': form})

def list_user_types(request):
    user_types = UserType.objects.all()
    return render(request, 'list_user_types.html', {'user_types': user_types})

def solicitudes(request):
    return render(request, 'solicitudes.html')

def index(request):
    return render(request, 'index.html')



def user_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenido {user.username}!")
                return redirect('index')  # Redirigir a la vista 'index'
            else:
                messages.error(request, "Usuario o contraseña incorrectos")
        else:
            messages.error(request, "Formulario no válido")
    else:
        form = CustomLoginForm()

    return render(request, 'login.html', {'form': form})