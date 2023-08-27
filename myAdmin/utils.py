from custom_token.models import CustomToken
# from myAdmin.models import myAdmin  # Import your custom user model
import random
import string
def get_custom_token(user):
    try:
        custom_token = CustomToken.objects.get(user=user)
        return custom_token
    except CustomToken.DoesNotExist:
        return None

def create_custom_token(user):
    # Generate a random token key
    token_key = ''.join(random.choices(string.ascii_letters + string.digits, k=40))

    # Create a new CustomToken object and associate it with the user
    custom_token = CustomToken(user=user, key=token_key)
    custom_token.save()

    return custom_token
