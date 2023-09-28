from django.urls import path 
from .views import professorList, professorCreate, professorLogin, set_grade, studentList, getProtest, deleteProtest 
urlpatterns = [
    path('' , professorList, name= 'professor_list'), 
    path('create/' , professorCreate, name= 'professor_create'),
    path('login/', professorLogin, name= 'professor_login'),
    path('setgrade/', set_grade, name='set_student_grade'),
    path('students/', studentList, name='student_list'),
    path('protests/', getProtest, name='prosets'),
    path('deleteProtest/<str:studentID>' , deleteProtest, name= 'delete_protest'),
]
