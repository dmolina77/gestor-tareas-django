from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    class Rol(models.TextChoices):
        ADMIN = "admin", "Administrador"
        USUARIO = "usuario", "Usuario"

    email = models.EmailField(unique=True)
    rol = models.CharField(
        max_length=20,
        choices=Rol.choices,
        default=Rol.USUARIO,
    )
