from django.urls import path
from .views import facultyList, facultyCreate
urlpatterns = [
    path('', facultyList, name= 'faculty_List'),
    path('create/', facultyCreate, name= 'faculty_create' )
]
