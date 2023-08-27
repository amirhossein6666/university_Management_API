from django.db import models
from myAdmin.models import myAdmin
from professor.models import professor
from student.models import student
class AdminCustomToken(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    user = models.OneToOneField(myAdmin, on_delete=models.CASCADE, related_name='custom_token')

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Custom Token'

    def __str__(self):
        return self.user.username

class ProfessorCustomToken(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    user = models.OneToOneField(professor, on_delete=models.CASCADE, related_name='custom_token')

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Custom Token'

    def __str__(self):
        return self.user.username

class StudentCustomToken(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    user = models.OneToOneField(student, on_delete=models.CASCADE, related_name='custom_token')

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Custom Token'

    def __str__(self):
        return self.user.username