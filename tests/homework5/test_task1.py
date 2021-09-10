import datetime

import pytest

from homework5.task1 import Homework, Student, Teacher

FAKE_TIME = datetime.datetime(2021, 9, 10, 17, 5, 55)


@pytest.fixture
def patch_datetime_now(monkeypatch):

    class mydatetime:
        @classmethod
        def now(cls):
            return FAKE_TIME

    monkeypatch.setattr(datetime, 'datetime', mydatetime)


@pytest.fixture
def setup_test_classes(patch_datetime_now):
    student = Student('Roman', 'Petrov')
    teacher = Teacher('Daniil', 'Shadrin')
    expired_homework = teacher.create_homework('Learn functions', 0)
    active_homework = teacher.create_homework('create 2 simple classes', 150)
    return {'student': student,
            'teacher': teacher,
            'expired_homework': expired_homework,
            'active_homework': active_homework}


def test_student_attributes(setup_test_classes):
    student = setup_test_classes['student']
    assert student.first_name == 'Roman'
    assert student.last_name == 'Petrov'


def test_teacher_attributes(setup_test_classes):
    teacher = setup_test_classes['teacher']
    assert teacher.first_name == 'Daniil'
    assert teacher.last_name == 'Shadrin'


def test_homework_attributes(setup_test_classes):
    expired_homework = setup_test_classes['expired_homework']
    active_homework = setup_test_classes['active_homework']
    assert str(expired_homework.deadline) == '0:00:00'
    assert expired_homework.text == 'Learn functions'
    assert str(active_homework.deadline) == '150 days, 0:00:00'
    assert active_homework.text == 'create 2 simple classes'
    assert active_homework.created == FAKE_TIME


def test_student_methods(setup_test_classes):
    student = setup_test_classes['student']
    expired_homework = setup_test_classes['expired_homework']
    active_homework = setup_test_classes['active_homework']
    assert student.do_homework(expired_homework) == 'You are late'
    assert student.do_homework(active_homework) == active_homework


def test_teacher_methods(setup_test_classes):
    teacher = setup_test_classes['teacher']
    assert isinstance(teacher.create_homework('Learn functions', 0), Homework)


def test_homework_methods(setup_test_classes):
    active_homework = setup_test_classes['active_homework']
    expired_homework = setup_test_classes['expired_homework']
    assert active_homework.is_active()
    assert not expired_homework.is_active()
