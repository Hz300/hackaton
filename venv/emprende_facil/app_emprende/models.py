from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.



class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    unidades = models.IntegerField()

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    idcliente = models.CharField(max_length=20, unique=True)
    domicilio = models.CharField(max_length=255, blank=True, null=True)
    rfc = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    regimen_fiscal = models.CharField(max_length=100, blank=True, null=True)
    cfdi = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE, null=True)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=True)
    fecha_venta = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Venta de {self.cantidad} {self.producto.nombre} a {self.cliente.nombre} el {self.fecha_venta}"

class VentaDetalle(models.Model):
    venta = models.ForeignKey('Venta', on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad_venta = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle de venta {self.id} - {self.cantidad_venta} {self.producto.nombre} (Total: {self.total})"

# Función para recalcular el total del detalle de venta
def recalcular_total_venta_detalle(sender, instance, created, **kwargs):
    if created:
        instance.total = instance.venta.producto.precio * instance.cantidad_venta
        instance.save()

# Conecta la señal post_save con la función recalcular_total_venta_detalle
post_save.connect(recalcular_total_venta_detalle, sender=VentaDetalle)
    





class Usuario(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, null=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    nombre_empresa = models.CharField(max_length=255)
    nivel = models.IntegerField(default=0)
    

    # Specify unique related_name attributes to resolve the clash
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_('groups'),
        blank=True,
        related_name='usuarios',  # Use a unique related_name
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_query_name='usuario',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        related_name='usuarios',  # Use a unique related_name
        help_text=_('Specific permissions for this user.'),
        related_query_name='usuario',
    )

###username: A unique identifier for the user, often used for authentication.
##first_name: The user's first name.
##last_name: The user's last name.
##email: The user's email address.
##password: The user's password (stored as a hash).
##is_staff: A boolean indicating whether the user is allowed to access the admin site.
#is_active: A boolean indicating whether the user account is active.
#date_joined: The date and time when the user account was created.