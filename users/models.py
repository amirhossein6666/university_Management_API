from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, role=None, **extra_fields):
        if not username:
            raise ValueError(_('The Username field must be set'))

        user = self.model(username=username, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, role=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(username, password, role, **extra_fields)


class customUser(AbstractBaseUser, PermissionsMixin):
    role= models.CharField(max_length=50)
    username=models.CharField(max_length=50, unique=True)
    password= models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  
    is_superuser = models.BooleanField(default=False) 
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['role']

    objects = CustomUserManager()

    def get_by_natural_key(self, username):
        return self.get(username=username)

    def __str__(self):
        return self.username + "  as  " + self.role
    