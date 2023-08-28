from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import course
from .serializers import courseSerializers
from rest_framework.response import Response
from rest_framework import status
from faculty.models import faculty
from professor.models import professor
from core.permissions import IsAdminUser
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def courseList(request):
    courses = course.objects.all()
    serializedCourses = courseSerializers(courses, many=True)
    return Response(serializedCourses.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def courseCreate(request):
    if request.method == 'POST':
        professorName = request.data['professor']
        courseProfessor = professor.objects.get(username=professorName, role='professor')
        myCourseFaculty = courseProfessor.faculty
        myCourse = {
            'name' : request.data['name'],
            'professor' : courseProfessor.id,
            'courseFaculty': myCourseFaculty.id
        }
        serializedcourse = courseSerializers(data=myCourse)
        if serializedcourse.is_valid():
            serializedcourse.save()
            myCourseFaculty.courses.add(course.objects.get(name=request.data['name']).id)
            return Response(serializedcourse.data, status=status.HTTP_201_CREATED)
        return Response(serializedcourse.errors, status=status.HTTP_400_BAD_REQUEST)
