from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UsuarioForm, CustomAuthenticationForm
from django.contrib.auth.forms import AuthenticationForm

 
def signup(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UsuarioForm()
    return render(request, 'app_emprende/signup.html', {'form': form})

def user_login(request):
    error_message = None
    print("Inside user_login function")  # Add this debug print
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("User logged in successfully")  # Add this debug print
                # Redirect to a success page or wherever you want
                return redirect('index')
            else:
                # Handle invalid login credentials
                error_message = "Invalid username or password."
    else:
        form = CustomAuthenticationForm()
        error_message = None
    return render(request, 'app_emprende/login.html', {'form': form, 'error_message': error_message})

def user_logout(request):
    logout(request)
    return redirect('app_emprende/login.html')
