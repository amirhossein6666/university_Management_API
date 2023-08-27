from django.db import models
# from professor.models import professor
# from course.models import course
from django.contrib.auth.models import AbstractUser, Group, Permission
class student(AbstractUser):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    professors = models.ManyToManyField('professor.professor')
    courses = models.ManyToManyField('course.course')
    grade = models.IntegerField()

    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='students_groups'  # Custom related_name for students
    )

    # Add a custom related_name for the user_permissions relationship
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name='students_user_permissions'  # Custom related_name for students
    )
    def __str__(self):
        return self.name