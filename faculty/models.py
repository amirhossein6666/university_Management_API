from django.db import models
# from course.models import course
from django.apps import apps
class faculty(models.Model): 
    name = models.CharField(max_length=50)
    courses = models.ForeignKey('course.course', on_delete=models.CASCADE)

    def __str__(self):
        return self.name