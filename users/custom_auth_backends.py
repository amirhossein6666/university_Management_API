from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import customUser

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, role=None, **kwargs):
        try:
            user = customUser.objects.get(username=username, role=role, password=password)
            return user
        except customUser.DoesNotExist:
            return None

        # if user.check_password(password):
        #     return user

    # def get_user(self, user_id):
    #     try:
    #         return User.objects.get(pk=user_id)
    #     except User.DoesNotExist:
    #         return None
