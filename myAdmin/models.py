from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class AdminManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('The Username field must be set')
        
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Admin(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AdminManager()

    USERNAME_FIELD = 'username'

    groups = models.ManyToManyField(
        'auth.Group',  # You can also use 'myAdmin.Group' if you've defined a custom Group model
        related_name='admin_users'  # This is the related name to avoid clashes
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',  # You can also use 'myAdmin.Permission' if you've defined a custom Permission model
        related_name='admin_users'  # This is the related name to avoid clashes
    )

    def __str__(self):
        return self.username
    