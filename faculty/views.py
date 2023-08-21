from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import faculty
from .serializers import facultySerializers
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def facultyList(request):
    faculties = faculty.objects.all()
    serilizedFaculties = facultySerializers(faculties, many= True)
    return Response(serilizedFaculties.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def facultyCreate(request):
    if request.method == 'POST':
        serilizedFaculty = facultySerializers(data=request.data)
        if serilizedFaculty.is_valid():
            serilizedFaculty.save()
            return Response (serilizedFaculty.data, status=status.HTTP_201_CREATED)
        return Response(serilizedFaculty.errors, status=status.HTTP_400_BAD_REQUEST)
