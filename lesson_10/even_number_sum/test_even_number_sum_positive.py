import pytest

from lesson_07.homework_07 import even_number_sum

input_values = [range(11), list(range(-11,0)), []]
expected = [30, -30, 0]
zip_params = list(zip(input_values, expected))


@pytest.mark.positive
@pytest.mark.even_number_sum
@pytest.mark.parametrize("input_values, expected", zip_params)
def test_even_number_sum_positive(input_values, expected):
    assert even_number_sum(input_values) == expected
