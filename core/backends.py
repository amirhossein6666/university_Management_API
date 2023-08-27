from django.contrib.auth.backends import ModelBackend
from professor.models import professor
from myAdmin.models import myAdmin
from student.models import student
class ProfessorBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = professor.objects.get(username=username)
        except professor.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None

class StudentBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = student.objects.get(username=username)
        except student.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None

class AdminBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):

        try:
            user = myAdmin.objects.get(username=username, password=password)
        except myAdmin.DoesNotExist:
            return None
        if user:
            return user
        return None
