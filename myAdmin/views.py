from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
# from django.contrib.auth import authenticate
from .serializers import adminSerializers
from .models import myAdmin
from rest_framework.authtoken.models import Token
from core.backends import AdminBackend
from custom_token.models import CustomToken
from .utils import get_custom_token, create_custom_token
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def adminCreate(request):
    if request.method == 'POST':
        serializedAdmin = adminSerializers(data=request.data)
        if serializedAdmin.is_valid():
            serializedAdmin.save()
            return Response(serializedAdmin.data , status=status.HTTP_201_CREATED)
        return Response(serializedAdmin.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def adminLogin(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        my_admin =AdminBackend().authenticate(request, username=username, password=password)
        if my_admin:
            Custom_token = get_custom_token(my_admin)
            if not Custom_token:
                Custom_token = create_custom_token(my_admin)
            return Response({'token': Custom_token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)  