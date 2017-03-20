from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Classroom(models.Model):
    user = models.ForeignKey(User, default=1)
    classroom_title = models.CharField(max_length=500)
    def __str__(self):
        return self.classroom_title



class Student(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=50)
    mark = models.IntegerField(default=0)

    def __str__(self):
        return self.student_name
