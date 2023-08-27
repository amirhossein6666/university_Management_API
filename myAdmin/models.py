from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, PermissionsMixin
from django.contrib.auth.backends import ModelBackend

class myAdmin(AbstractUser, PermissionsMixin):
    username= models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(default="admin", max_length=40)
    # auth_backend = 'custom_token.custom_token_backend.CustomTokenBackend'

    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='myadmin_groups'  # Custom related_name for myAdmin
    )

    # Add a custom related_name for the user_permissions relationship
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name='myadmin_user_permissions'  # Custom related_name for myAdmin
    )
    def __str__(self):
        return self.username
    