from django.urls import path 
from .views import professorList, professorCreate, professorLogin
urlpatterns = [
    path('' , professorList, name= 'professor_list'), 
    path('create/' , professorCreate, name= 'professor_create'),
    path('login/', professorLogin, name= 'professor_login')
]
