from django.urls import path 
from .views import studentList, studentCreate, studentLogin
urlpatterns = [
    path('', studentList, name="stu_list"),
    path('create/', studentCreate, name= "stu_create"),
    path('login/', studentLogin, name ="stu_login")
]
