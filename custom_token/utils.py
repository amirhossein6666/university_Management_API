from .models import AdminCustomToken, ProfessorCustomToken, StudentCustomToken
# from myAdmin.models import myAdmin  # Import your custom user model
import random
import string
def admin_get_custom_token(user):
    try:
        custom_token = AdminCustomToken.objects.get(user=user)
        return custom_token
    except AdminCustomToken.DoesNotExist:
        return None

def admin_create_custom_token(user):
    # Generate a random token key
    token_key = ''.join(random.choices(string.ascii_letters + string.digits, k=40))

    # Create a new CustomToken object and associate it with the user
    custom_token = AdminCustomToken(user=user, key=token_key)
    custom_token.save()

    return custom_token

def professor_get_custom_token(user):
    try:
        custom_token = ProfessorCustomToken.objects.get(user=user)
        return custom_token
    except ProfessorCustomToken.DoesNotExist:
        return None

def professor_create_custom_token(user):
    # Generate a random token key
    token_key = ''.join(random.choices(string.ascii_letters + string.digits, k=40))

    # Create a new CustomToken object and associate it with the user
    custom_token = ProfessorCustomToken(user=user, key=token_key)
    custom_token.save()

    return custom_token

def student_get_custom_token(user):
    try:
        custom_token = StudentCustomToken.objects.get(user=user)
        return custom_token
    except StudentCustomToken.DoesNotExist:
        return None

def student_create_custom_token(user):
    # Generate a random token key
    token_key = ''.join(random.choices(string.ascii_letters + string.digits, k=40))

    # Create a new CustomToken object and associate it with the user
    custom_token = StudentCustomToken(user=user, key=token_key)
    custom_token.save()

    return custom_token