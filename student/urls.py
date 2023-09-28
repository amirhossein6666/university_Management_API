from django.urls import path 
from .views import studentList, studentCreate, studentLogin, courseEnroll, courseList, gradeList , sendProtests
urlpatterns = [
    path('', studentList, name="stu_list"),
    path('create/', studentCreate, name= "stu_create"),
    path('login/', studentLogin, name ="stu_login"),
    path('enroll/', courseEnroll, name='enroll_in_course'),
    path('courses/', courseList, name= 'course_list'),
    path('grades/', gradeList, name='grade_list'),
    path('sendProtest/', sendProtests, name= 'send_protest')
]
    