from django.contrib.auth.backends import ModelBackend
from .models import AdminCustomToken, ProfessorCustomToken, StudentCustomToken
class AdminCustomTokenBackend(ModelBackend):
    def authenticate(self, request):
        # Get the "Authorization" header from the request
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if auth_header and auth_header.startswith('Token '):
            # Extract the token key from the header (remove "Token " prefix)
            token_key = auth_header[6:]

            try:
                custom_token = AdminCustomToken.objects.get(key=token_key)

                return (custom_token.user,"test")
            except AdminCustomToken.DoesNotExist:
                return None

        # If the header is missing or doesn't start with "Token ", return None
        return None

class professorCustomTokenBackend(ModelBackend):
    def authenticate(self, request):
        # Get the "Authorization" header from the request
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if auth_header and auth_header.startswith('Token '):
            # Extract the token key from the header (remove "Token " prefix)
            token_key = auth_header[6:]

            try:
                custom_token = ProfessorCustomToken.objects.get(key=token_key)

                return (custom_token.user,"test")
            except ProfessorCustomToken.DoesNotExist:
                return None

        # If the header is missing or doesn't start with "Token ", return None
        return None

class studentCustomTokenBackend(ModelBackend):
    def authenticate(self, request):
        # Get the "Authorization" header from the request
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if auth_header and auth_header.startswith('Token '):
            # Extract the token key from the header (remove "Token " prefix)
            token_key = auth_header[6:]

            try:
                custom_token = StudentCustomToken.objects.get(key=token_key)

                return (custom_token.user,"test")
            except StudentCustomToken.DoesNotExist:
                return None

        # If the header is missing or doesn't start with "Token ", return None
        return None  