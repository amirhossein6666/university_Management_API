from django.db import models
# from professor.models import professor
# from student.models import student
class course(models.Model): 
    name = models.CharField(max_length=50)
    professor = models.ForeignKey('professor.professor', on_delete=models.CASCADE)
    students = models.ManyToManyField('student.student')

    def __str__(self):
        return self.name