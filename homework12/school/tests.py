import datetime

from django.test import TestCase
from school.models import Homework, HomeworkResult, Student, Teacher


class AnimalTestCase(TestCase):
    def setUp(self):
        Student.objects.create(firstname="Иван", lastname="Петров")
        Teacher.objects.create(firstname="Петр", lastname="Иванов")
        Homework.objects.create(deadline="2025-10-20 12:49:50",
                                is_active=True)
        student = Student.objects.all()[0]
        teacher = Teacher.objects.all()[0]
        homework = Homework.objects.all()[0]
        HomeworkResult.objects.create(homework=homework,
                                      student=student,
                                      teacher=teacher,
                                      completed_date='2025-10-25 12:49:50',
                                      solution='Solution for the hw')

    def test_student(self):
        student = Student.objects.all()[0]
        self.assertEqual(student.firstname, 'Иван')
        self.assertEqual(student.lastname, 'Петров')

    def test_teacher(self):
        teacher = Teacher.objects.all()[0]
        self.assertEqual(teacher.firstname, 'Петр')
        self.assertEqual(teacher.lastname, 'Иванов')

    def test_homework(self):
        homework = Homework.objects.all()[0]
        self.assertEqual(homework.created.strftime('%Y-%m-%d %H:%M'),
                         datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
        self.assertEqual(homework.deadline.strftime('%Y-%m-%d %H:%M'),
                         "2025-10-20 12:49")
        self.assertEqual(homework.is_active, True)

    def test_homework_result(self):
        student = Student.objects.all()[0]
        teacher = Teacher.objects.all()[0]
        homework = Homework.objects.all()[0]

        homework_result = HomeworkResult.objects.all()[0]
        self.assertEqual(homework_result.homework, homework)
        self.assertEqual(homework_result.student, student)
        self.assertEqual(homework_result.teacher, teacher)
        self.assertEqual(homework_result.completed_date.strftime('%Y-%m-%d %H:%M'),
                         '2025-10-25 12:49')
        self.assertEqual(homework_result.solution, 'Solution for the hw')
