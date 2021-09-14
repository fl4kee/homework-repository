"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime
1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истекло ли время на выполнение задания,
    возвращает boolean
2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None
3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime


class Student:
    def __init__(self, first_name, last_name):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def do_homework(homework):
        if homework.is_active():
            return homework
        else:
            return 'You are late'


class Teacher:
    def __init__(self, first_name, last_name):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def create_homework(task, days):
        return Homework(task, days)


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
