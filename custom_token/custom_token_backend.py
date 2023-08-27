from django.contrib.auth.backends import ModelBackend
from .models import CustomToken

class CustomTokenBackend(ModelBackend):
    def authenticate(self, request, token=None):
        try:
            custom_token = CustomToken.objects.get(key=token)
            return custom_token.user
        except CustomToken.DoesNotExist:
            return None