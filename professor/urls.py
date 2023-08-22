from django.urls import path 
from .views import professorList, professorCreate
urlpatterns = [
    path('' , professorList, name= 'professor_list'), 
    path('create/' , professorCreate, name= 'professor_create')
]
