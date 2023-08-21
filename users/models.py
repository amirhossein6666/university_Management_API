from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class customUser(AbstractBaseUser, PermissionsMixin):
    role= models.CharField(max_length=50)
    username=models.CharField(max_length=50, unique=True)
    password= models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['role']

    def __str__(self):
        return self.username + "  as  " + self.role
    