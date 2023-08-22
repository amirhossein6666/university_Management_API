from django.db import models
from faculty.models import faculty
from student.models import student
class professor(models.Model): 
    name = models.CharField(max_length=50)
    faculty = models.ForeignKey(faculty, on_delete=models.CASCADE)
    students = models.ManyToManyField(student, blank=True , null= True)

    def __str__(self):
        return self.name