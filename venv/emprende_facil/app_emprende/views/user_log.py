from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UsuarioForm, CustomAuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages  # Import messages framework

 
def signup(request):
    print("Inside signup function")
    
    if request.method == 'POST':
        print("Request method is POST")
        form = UsuarioForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            form.save()
            return redirect('login')
        else:
            print("Form is invalid")
            print(form.errors)  # Print form errors for debugging
    else:
        print("Request method is not POST")
        form = UsuarioForm()
    
    return render(request, 'app_emprende/signup.html', {'form': form})


def user_login(request):
    error_message = None
    
    print("Inside user_login function")  # Add this debug print

    if request.method == 'POST':
        print("using post method")
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            print("form is valid")
            username = form.cleaned_data['username']
            print(username)
            password = form.cleaned_data['password']
            print(password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                print("user is not none")
                login(request, user)
                print("User logged in successfully")  # Add this debug print
                # Redirect to a success page or wherever you want
                return redirect('index')
            else:
                error_message = "Invalid username or password."
                print(error_message)
                messages.error(request, error_message)  # Add error message using messages framework
        else:
            error_message = "Form is invalid."
            print(error_message)
            messages.error(request, error_message)  # Add error message using messages framework
    else:
        form = CustomAuthenticationForm()
        error_message = "No POST request received."
        print(error_message)

    # Add form errors to the messages framework
    for field, errors in form.errors.items():
        for error in errors:
            messages.error(request, f"{field}: {error}")

    return render(request, 'app_emprende/login.html', {'form': form})
    

def user_logout(request):
    logout(request)
    return redirect('app_emprende/login.html')
