from django.db import models
# from professor.models import professor
# from course.models import course
class student(models.Model):
    name = models.CharField(max_length=50)
    professors = models.ManyToManyField('professor.professor')
    courses = models.ManyToManyField('course.course')
    grade = models.IntegerField()

    def __str__(self):
        return self.name