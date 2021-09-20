import datetime

import pytest

from homework6.task2 import (DeadlineError, Homework, HomeworkResult, Student,
                             Teacher)

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
    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')
    oop_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')
    oop_hw = oop_teacher.create_homework('Learn OOP', 100)
    result_oop_hw = good_student.do_homework(oop_hw, 'I have done this hw')
    wrong_result_oop_hw = good_student.do_homework(oop_hw, 'done')
    expired_homework = oop_teacher.create_homework('Learn functions', 0)
    active_homework = oop_teacher.create_homework('create 2 simple classes', 150)
    return {'lazy_student': lazy_student,
            'good_student': good_student,
            'oop_teacher': oop_teacher,
            'advanced_python_teacher': advanced_python_teacher,
            'oop_hw': oop_hw,
            'result_oop_hw': result_oop_hw,
            'wrong_result_oop_hw': wrong_result_oop_hw,
            'expired_homework': expired_homework,
            'active_homework': active_homework
            }


def test_student_attributes(setup_test_classes):
    lazy_student = setup_test_classes['lazy_student']
    good_student = setup_test_classes['good_student']
    assert lazy_student.first_name == 'Roman'
    assert good_student.last_name == 'Sokolov'


def test_teacher_attributes(setup_test_classes):
    oop_teacher = setup_test_classes['oop_teacher']
    advanced_python_teacher = setup_test_classes['advanced_python_teacher']
    assert oop_teacher.first_name == 'Daniil'
    assert advanced_python_teacher.last_name == 'Smetanin'


def test_homework_attributes(setup_test_classes):
    expired_homework = setup_test_classes['expired_homework']
    active_homework = setup_test_classes['active_homework']
    assert str(expired_homework.deadline) == '0:00:00'
    assert expired_homework.text == 'Learn functions'
    assert str(active_homework.deadline) == '150 days, 0:00:00'
    assert active_homework.text == 'create 2 simple classes'
    assert active_homework.created == FAKE_TIME


def test_homework_result_attributes(setup_test_classes):
    result_oop_hw = setup_test_classes['result_oop_hw']
    good_student = setup_test_classes['good_student']
    assert result_oop_hw.created == FAKE_TIME
    assert result_oop_hw.solution == 'I have done this hw'
    assert result_oop_hw.author is good_student


def test_homework_result_exception(setup_test_classes):
    good_student = setup_test_classes['good_student']
    with pytest.raises(ValueError, match='You gave a not Homework object'):
        HomeworkResult(good_student, "fff", "Solution")


def test_expired_homework_exception(setup_test_classes):
    lazy_student = setup_test_classes['lazy_student']
    expired_homework = setup_test_classes['expired_homework']
    with pytest.raises(DeadlineError, match='You are late'):
        lazy_student.do_homework(expired_homework, 'done')


def test_student_methods(setup_test_classes):
    good_student = setup_test_classes['good_student']
    oop_hw = setup_test_classes['oop_hw']
    assert isinstance(good_student.do_homework(oop_hw, 'I have done this hw too'), HomeworkResult)


def test_teacher_methods(setup_test_classes):
    oop_teacher = setup_test_classes['oop_teacher']
    oop_hw = setup_test_classes['oop_hw']
    wrong_result_oop_hw = setup_test_classes['wrong_result_oop_hw']
    result_oop_hw = setup_test_classes['result_oop_hw']
    assert isinstance(oop_teacher.create_homework('Learn functions', 0), Homework)
    assert oop_teacher.check_homework(result_oop_hw) is True
    assert bool(Teacher.completed_homeworks) is True
    assert oop_teacher.check_homework(wrong_result_oop_hw) is False
    assert isinstance(Teacher.completed_homeworks[oop_hw], HomeworkResult)
    Teacher.reset_results()
    assert bool(Teacher.completed_homeworks) is False


def test_homework_methods(setup_test_classes):
    active_homework = setup_test_classes['active_homework']
    expired_homework = setup_test_classes['expired_homework']
    assert active_homework.is_active()
    assert not expired_homework.is_active()
