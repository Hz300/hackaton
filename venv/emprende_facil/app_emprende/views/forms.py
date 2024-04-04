from django import forms
from ..models import Producto, Cliente, Usuario, Venta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.text import slugify
# from .forms import VentaDetalleFormSet
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'costo', 'precio_venta', 'unidades']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Agrega el atributo de datos 'precio-venta' a cada opción del campo 'producto'
        # self.fields['producto'].widget.choices = [(producto.id, producto.nombre, {'data-precio_venta': producto.precio_venta}) for producto in Producto.objects.all()]


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono', 'domicilio', 'rfc', 'email', 'regimen_fiscal', 'cfdi']

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['producto', 'cliente', 'cantidad']
        labels = {
            'producto': 'Producto',
            'cliente': 'Cliente',
            'cantidad': 'Cantidad vendida',
           
        }
        widgets = {
            'nombre': forms.Select(attrs={'id': 'nombre'}),  # Asegúrate de que el ID sea 'id_producto'
            'unidad': forms.NumberInput(attrs={'id': 'unidad', 'min': 1}),  # Asegúrate de que el ID sea 'id_cantidad'
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # Modifica las opciones del campo 'producto' para incluir el precio de venta como un atributo de datos
    #     self.fields['nombre'].widget.choices = [
    #         (producto.id, producto.nombre, {'data-precio_venta': producto.precio_venta})
    #         for producto in Producto.objects.all()
    #     ]

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'email', 'password1', 'password2', 'nombre_empresa', 'username']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control w-75 bg-transparent border-bottom text-body'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control w-75 bg-transparent border-bottom text-body'}),
            'email': forms.TextInput(attrs={'class': 'form-control w-75 bg-transparent border-bottom text-body'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control w-75 bg-transparent border-bottom text-body'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control w-75 bg-transparent border-bottom text-body'}),
            'nombre_empresa': forms.TextInput(attrs={'class': 'form-control w-75 bg-transparent border-bottom text-body'}),
            'username': forms.TextInput(attrs={'class': 'form-control w-75 bg-transparent border-bottom text-body'}),
        }
       
        def save(self, commit=True):
            user = super().save(commit=False)  # Call parent form's save (don't commit yet)
            user.set_password(self.cleaned_data['password1'])  # Set password on custom model
            if commit:
                user.save()  # Save the user to your custom model's table
            return user



    

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password']

    

