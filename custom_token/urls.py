from django.urls import path, include
from .views import adminTokenList, professorTokenList, studentTokenList
urlpatterns = [
    path('admin/', adminTokenList),
    path('professor/', professorTokenList),
    path('student/', studentTokenList)
]
