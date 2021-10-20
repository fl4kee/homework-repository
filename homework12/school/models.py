from django.db import models


# Create your models here.
class Student(models.Model):

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class Teacher(models.Model):

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class Homework(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    is_active = models.BooleanField(default=True)


class HomeworkResult(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    completed_date = models.DateTimeField()
    solution = models.CharField(max_length=100)
