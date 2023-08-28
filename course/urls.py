from django.urls import path 
from .views import courseList , courseCreate
urlpatterns = [
    path('' , courseList, name='course_list'),
    path('create/', courseCreate, name= 'course_create'),
]
