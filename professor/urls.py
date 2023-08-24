from django.urls import path 
from .views import professorList
urlpatterns = [
    path('' , professorList, name= 'professor_list'), 
]
