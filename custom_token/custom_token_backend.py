from django.contrib.auth.backends import ModelBackend
from .models import CustomToken
import pdb
class CustomTokenBackend(ModelBackend):
    def authenticate(self, request):
        # Get the "Authorization" header from the request
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if auth_header and auth_header.startswith('Token '):
            # Extract the token key from the header (remove "Token " prefix)
            token_key = auth_header[6:]

            try:
                custom_token = CustomToken.objects.get(key=token_key)

                return (custom_token.user,"test")
            except CustomToken.DoesNotExist:
                return None

        # If the header is missing or doesn't start with "Token ", return None
        return None