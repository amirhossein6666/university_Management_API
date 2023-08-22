from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from .serializers import UserSerializer
from myAdmin.models import Admin
from rest_framework.authtoken.models import Token
from .custom_auth_backends import CustomBackend

# @api_view(['POST'])
# def createUser(request):
#     serialized_user = UserSerializer(data=request.data)
#     if serialized_user.is_valid():
#         serialized_user.save()
#         return Response(serialized_user.data, status=status.HTTP_201_CREATED)
#     return Response(serialized_user.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        role = request.data.get('role') 
        if role == 'professor':
            prof = CustomBackend().professor_authenticate(request, username=username, password=password)
            if prof:
                token, created = Token.objects.get_or_create(user=prof)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        if role == 'student':
            stu = CustomBackend().student_authenticate(request, username=username, password=password)
            if stu:
                token, created = Token.objects.get_or_create(user=stu)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        if role == 'admin':
            admin = CustomBackend().admin_authenticate(request, username=username, password=password)
            if admin:
                token, created = Token.objects.get_or_create(user=admin)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
               
