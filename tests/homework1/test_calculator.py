import pytest

from homework1.calculator.calc import check_power_of_2


@pytest.mark.parametrize(
    "test_input,expected",
    [(65536, True), (12, False), (0, False), (-4, False), (2, True)],
)
def test_check_power_of_2(test_input, expected):
    assert check_power_of_2(test_input) == expected
