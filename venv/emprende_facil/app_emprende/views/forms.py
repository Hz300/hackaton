from django import forms
from ..models import Producto
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.text import slugify
from ..models import Usuario
from django.contrib.auth.forms import AuthenticationForm

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'email', 'password', 'nombre_empresa','username',]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control w-75 bg-transparent border-bottom text-body'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control w-75 bg-transparent border-bottom text-body'}),
            'email': forms.TextInput(attrs={'class': 'form-control w-75 bg-transparent border-bottom text-body'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control w-75 bg-transparent border-bottom text-body'}),
            'nombre_empresa': forms.TextInput(attrs={'class': 'form-control w-75 bg-transparent border-bottom text-body'}),
            'username': forms.TextInput(attrs={'class': 'form-control w-75 bg-transparent border-bottom text-body'}),
        }
       

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()

    

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password']

    

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'costo', 'precio_venta', 'unidades']