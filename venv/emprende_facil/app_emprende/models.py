from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    unidades = models.IntegerField()

    def __str__(self):
        return self.nombre



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