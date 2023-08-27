from django.db import models
from faculty.models import faculty
from student.models import student
from django.contrib.auth.models import AbstractUser, Group, Permission
class professor(AbstractUser): 
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    faculty = models.ForeignKey(faculty, on_delete=models.CASCADE)
    students = models.ManyToManyField(student, blank=True , null= True)
    role = models.CharField(default="professor", max_length=40)
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='professors_groups'  # Custom related_name for professors
    )

    # Add a custom related_name for the user_permissions relationship
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name='professors_user_permissions'  # Custom related_name for professors
    )


    def __str__(self):
        return self.name