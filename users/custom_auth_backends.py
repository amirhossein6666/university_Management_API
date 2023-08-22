from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from professor.models import professor
from student.models import student
from myAdmin.models import Admin

class CustomBackend(ModelBackend):
    def professor_authenticate(self, request, username=None, password=None, **kwargs):
        try:
            prof = professor.objects.get(username=username, password=password)
            return prof
        except professor.DoesNotExist:
            return None
    def student_authenticate(self, request, username=None, password=None, **kwargs):
        try:
            stu = student.objects.get(username=username, password=password)
            return stu
        except student.DoesNotExist:
            return None
    def admin_authenticate(self, request, username=None, password=None, **kwargs):
        try:
            admin = Admin.objects.get(username=username, password=password)
            return admin
        except Admin.DoesNotExist:
            return None