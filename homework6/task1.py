"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls):
    class CounterClass(cls):
        counter = 0

        def __init__(self):
            self.increase_counter()

        @classmethod
        def increase_counter(cls):
            cls.counter += 1

        @classmethod
        def get_created_instances(cls):
            return cls.counter

        @classmethod
        def reset_instances_counter(cls):
            total_instances = cls.counter
            cls.counter = 0
            return total_instances

    return CounterClass
