from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import professor
from .serializers import professorSerializer
from faculty.models import faculty
from core.permissions import IsAdminUser
from core.backends import ProfessorBackend
from custom_token.utils import professor_get_custom_token, professor_create_custom_token
from .permissions import Is_professor
from student.models import student
from django.http import JsonResponse

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def professorList(request): 
    profList = professor.objects.all()
    serilizerdprofessor = professorSerializer(profList, many=True)
    return Response(serilizerdprofessor.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def professorCreate(request):
    if request.method == 'POST':
        facultyName = request.data['faculty']
        professorFaculty = faculty.objects.get(name=facultyName)
        myProfessor = {
            'username' : request.data['username'],
            'password' : request.data['password'],
            'faculty' : professorFaculty.id
        }
        serializedProfessor = professorSerializer(data=myProfessor)
        if serializedProfessor.is_valid():
            serializedProfessor.save()
            return Response(serializedProfessor.data, status=status.HTTP_201_CREATED)
        return Response(serializedProfessor.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def professorLogin(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        myProfessor = ProfessorBackend().authenticate(request, username=username, password= password)
        if myProfessor: 
            custom_token = professor_get_custom_token(myProfessor)
            if not custom_token:
                custom_token = professor_create_custom_token(myProfessor)
            return Response({'token': custom_token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated, Is_professor])
def set_grade(request):
    studentName = request.data['student']
    new_grade = request.data['grade']
    myProfessor = request.user
    try:
        myStudent = myProfessor.students.get(username=studentName)
    except student.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=404)
    myCourse = myStudent.courses.get(professor=myProfessor)
    flag = False
    if not myStudent.grades:
        flag = True
        myStudent.grades = {"test" : "testValue"}
    myStudent.grades.update({myCourse.id : int(new_grade)})
    if flag:
        myStudent.grades.pop("test")
    myStudent.save()
    return JsonResponse({'message': f'Grade updated to {new_grade}'})


