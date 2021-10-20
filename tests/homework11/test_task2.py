from homework11.task2 import Order


def test_order_strategy():
    def morning_discount(order):
        return order - order * 0.25

    def elder_discount(order):
        return order - order * 0.90

    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 75
    order_2 = Order(100, elder_discount)
    assert order_2.final_price() == 10
    order_3 = Order(100)
    assert order_3.final_price() == 100
