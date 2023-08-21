from django.db import models
# from course.models import course
from django.apps import apps
class faculty(models.Model): 
    name = models.CharField(max_length=50)
    courses = models.ManyToManyField('course.course', blank=True , null= True, related_name='facultyCourses')
    def add_course(self, course):   
        self.courses.add(course)
        
    def __str__(self):
        return self.name