from django.core.management.base import BaseCommand
from school.models import Homework, HomeworkResult, Student, Teacher

# python manage.py seed --mode=refresh

""" Clear all data and creates objects """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str)

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    print("Delete Address instances")
    Student.objects.all().delete()
    Teacher.objects.all().delete()
    Homework.objects.all().delete()
    HomeworkResult.objects.all().delete()


def create_student():
    student = Student(
        firstname='Иван',
        lastname='Петров',
    )
    student.save()
    return student


def create_teacher():
    teacher = Teacher(
        firstname='Петр',
        lastname='Иванов',
    )
    teacher.save()
    return teacher


def create_homework():
    homework = Homework(
        created='2021-10-20 12:49:50',
        deadline='2025-10-20 12:49:50',
        is_active=True
    )
    homework.save()
    return homework


def create_homework_result(student_inst, teacher_inst, homework_inst):
    homework_result = HomeworkResult(
        homework=homework_inst,
        student=student_inst,
        teacher=teacher_inst,
        completed_date='2021-10-25 12:49:50',
        solution='solution for the homework'
    )

    homework_result.save()


def run_seed(self, mode):
    """
    Seed database based on mode refrech or clear
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    student_inst = create_student()
    teacher_inst = create_teacher()
    homework_inst = create_homework()
    # Creating student

    create_homework_result(student_inst, teacher_inst, homework_inst)
