from homework4.task5 import fizzbuzz


def test_fizzbuzz():
    assert list(fizzbuzz(15)) == ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8',
                                  'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']
