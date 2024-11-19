from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'sobrenome']  # Campos obrigatórios no caso de criar superusuário

    # Remover o campo username, se necessário
    username = None

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuarios_groups',  # Evita o conflito de 'groups'
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios_user_permissions',  # Evita o conflito de 'user_permissions'
        blank=True,
    )

    def __str__(self):
        return self.email