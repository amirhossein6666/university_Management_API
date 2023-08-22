from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import professor
from .serializers import professorSerializer
from faculty.models import faculty
from core.permissions import IsAdminUser
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def professorList(request): 
    profList = professor.objects.all()
    serilizerdprofessor = professorSerializer(profList, many=True)
    return Response(serilizerdprofessor.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def professorCreate(request):
    if request.method == 'POST' :
        facultyName = request.data['faculty']
        myFaculty = faculty.objects.get(name=facultyName)
        professor = {
            'name' : request.data['name'],
            'faculty' : myFaculty.id,
        }
        print("test2")
        serializedProfessor = professorSerializer(data=professor)
        if serializedProfessor.is_valid():
            print("test")
            serializedProfessor.save()
            return Response(serializedProfessor.data, status=status.HTTP_201_CREATED)
        return Response(serializedProfessor.errors, status= status.HTTP_400_BAD_REQUEST)