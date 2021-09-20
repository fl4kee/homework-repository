"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict
from typing import Dict


class DeadlineError(Exception):
    pass


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Student(Person):
    def do_homework(self, homework, solution):
        if homework.is_active():
            done_homework = HomeworkResult(self, homework, solution)
            return done_homework
        else:
            raise DeadlineError('You are late')


class Teacher(Person):
    completed_homeworks: Dict = defaultdict(list)

    @staticmethod
    def create_homework(task, days):
        return Homework(task, days)

    @classmethod
    def check_homework(cls, homework):
        if len(homework.solution) > 5:
            cls.completed_homeworks[homework.homework] = homework
            return True
        return False

    @classmethod
    def reset_results(cls, *args):
        if not len(args):
            cls.completed_homeworks.clear()
        else:
            for arg in args:
                cls.completed_homeworks.pop(arg)


class HomeworkResult:
    def __init__(self, author, homework, solution):
        self.solution = solution
        if not isinstance(homework, Homework):
            raise ValueError('You gave a not Homework object')
        self.homework = homework
        self.author = author
        self.created = datetime.datetime.now()

    @property
    def created(self):
        return self._created

    @created.setter
    def created(self, value):
        self._created = value


class Homework:
    def __init__(self, text, days):
        self.text = text
        self.days = days
        self._created = datetime.datetime.now()

    @property
    def deadline(self):
        return datetime.timedelta(days=self.days)

    @property
    def created(self):
        return self._created

    @created.setter
    def created(self, value):
        self._created = value

    def is_active(self):
        current_time = datetime.datetime.now()
        return current_time + self.deadline > current_time
