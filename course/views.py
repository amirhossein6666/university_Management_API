from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import course
from .serializers import courseSerializers
from rest_framework.response import Response
from rest_framework import status
from faculty.models import faculty
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def courseList(request):
    courses = course.objects.all()
    serializedCourses = courseSerializers(courses, many=True)
    return Response(serializedCourses.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def courseCreate(request):
    if request.method == 'POST':
        professorName = request.data['professor']
        courseProfessor = customUser.objects.get(username=professorName, role='professor')
        facultyName = request.data['faculty']
        myCourseFaculty = faculty.objects.get(name=facultyName)
        myCourse = {
            'name' : request.data['name'],
            'professor' : courseProfessor.id,
            'courseFaculty': myCourseFaculty.id
        }
        serializedcourse = courseSerializers(data=myCourse)
        if serializedcourse.is_valid():
            serializedcourse.save()
            return Response(serializedcourse.data, status=status.HTTP_201_CREATED)
        return Response(serializedcourse.errors, status=status.HTTP_400_BAD_REQUEST)