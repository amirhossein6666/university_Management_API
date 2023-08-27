from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import student
from .serializers import studentSerializers
from core.permissions import IsAdminUser
from core.backends import StudentBackend
from custom_token.utils import student_get_custom_token, student_create_custom_token

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def studentList(request):
    stulist = student.objects.all()
    serializedStudents = studentSerializers(stulist, many=True)
    return Response (serializedStudents.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def studentCreate(request):
    if request.method == 'POST':
        serializedStudent = studentSerializers(data=request.data)
        if serializedStudent.is_valid():
            serializedStudent.save()
            return Response(serializedStudent.data, status=status.HTTP_201_CREATED)
        return Response(serializedStudent._errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
def studentLogin(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        myStudent = StudentBackend().authenticate(request, username=username, password=password)
        if myStudent:
            custom_token = student_get_custom_token(myStudent)
            if not custom_token:
                custom_token = student_create_custom_token(myStudent)
            return Response ({'token': custom_token.key}, status=status.HTTP_200_OK)
        return Response ({'error : Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            
