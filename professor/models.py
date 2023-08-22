from django.db import models
from faculty.models import faculty
from student.models import student
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class professorManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('The Username field must be set')
        
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # def create_superuser(self, username, password=None):
    #     user = self.create_user(username, password)
    #     user.is_staff = True
    #     user.is_superuser = True
    #     user.save(using=self._db)
    #     return user

class professor(AbstractBaseUser, PermissionsMixin): 
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    faculty = models.ForeignKey(faculty, on_delete=models.CASCADE)
    students = models.ManyToManyField(student, blank=True , null= True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = professorManager()

    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.username