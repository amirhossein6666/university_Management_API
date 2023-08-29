from django.urls import path 
from .views import professorList, professorCreate, professorLogin, set_grade, studentList
urlpatterns = [
    path('' , professorList, name= 'professor_list'), 
    path('create/' , professorCreate, name= 'professor_create'),
    path('login/', professorLogin, name= 'professor_login'),
    path('setgrade/', set_grade, name='set_student_grade'),
    path('students/', studentList, name='student_list')
]
