"""
You are given the following code:
class Order:
    morning_discount = 0.25
    def __init__(self, price):
        self.price = price
    def final_price(self):
        return self.price - self.price * self.morning_discount
Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy
Example of the result call:
def morning_discount(order):
    ...
def elder_discount(order):
    ...
order_1 = Order(100, morning_discount)
assert order_1.final_price() == 75
order_2 = Order(100, elder_discount)
assert order_2.final_price() == 10
"""
from typing import Callable, Union


class Order:
    def __init__(self, price: float, discount_strategy: Union[Callable, None] = None) -> None:
        self.price = price
        self.discount_strategy = discount_strategy

    def final_price(self) -> float:
        if self.discount_strategy:
            return self.discount_strategy(self.price)
        return self.price
