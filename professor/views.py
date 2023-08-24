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