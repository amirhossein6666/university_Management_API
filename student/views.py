from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import student
from .serializers import studentSerializers
from core.permissions import IsAdminUser
from core.backends import StudentBackend
from custom_token.utils import student_get_custom_token, student_create_custom_token
from course.models import course
from django.http import JsonResponse
from .permissions import Is_student
from course.serializers import courseSerializers
from professor.models import professor
@api_view(['GET'])
@permission_classes([IsAuthenticated])
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
            
@api_view(['POST'])
@permission_classes([IsAuthenticated, Is_student])
def courseEnroll(request):
    if request.method == 'POST':
        course_name = request.data['course']
        try:
            myCourse = course.objects.get(name=course_name)
        except course.DoesNotExist:
            return JsonResponse({'message': 'Course not found'}, status=404)

        student = request.user  
        myProfessor = myCourse.professor
        if student:
            student.courses.add(myCourse.id)  
            student.professors.add(myCourse.professor.id)
            myCourse.students.add(student.id)
            if myProfessor:
                myProfessor.students.add(student.id)
            return JsonResponse({'message': f'Enrolled in {course_name}'})

    return JsonResponse({'message': 'Invalid request'}, status=400)

@api_view(['GET'])
@permission_classes([Is_student, IsAuthenticated])
def courseList(request):
    myStudent = request.user
    courses = myStudent.courses.all()
    serializedCourse = courseSerializers(courses, many=True)
    return Response(serializedCourse.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated, Is_student])
def gradeList(request):
    mystudent = request.user
    grades =mystudent.grades
    gradeDict= {}
    for key in grades.keys():
        gradeDict.update({course.objects.get(pk=key).name : grades[key]})
    return JsonResponse(gradeDict, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated, Is_student])
def sendProtests(request): 
    protestText = request.data['body']
    professorReceiverID = request.data['professor']
    studentSender = request.user
    professorReceiver = professor.objects.get(pk=professorReceiverID)
    flag = False
    if not professorReceiver.protests: 
        flag = True
        professorReceiver.protests= {"test" : "testValue"}
    professorReceiver.protests.update({studentSender.id: protestText})
    if flag: 
        professorReceiver.protests.pop("test")
    professorReceiver.save()
    return JsonResponse({'message' : 'protest is sent'})
