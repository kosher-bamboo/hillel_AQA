import pytest

from lesson_07.homework_07 import even_number_sum

input_values = [range(11), [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11], []]
expected = [30, -30, 0]
zip_params = list(zip(input_values, expected))


@pytest.mark.positive
@pytest.mark.even_number_sum
@pytest.mark.parametrize("input_values, expected", zip_params)
def test_even_number_sum_positive(input_values, expected):
    assert even_number_sum(input_values) == expected
