import pytest
from lesson_07.homework_07 import arithmetic_mean

input_values = (("23", "24", "25"), ["2", "f"])
expected = (TypeError, TypeError)


@pytest.mark.negative
@pytest.mark.arithmetic_mean
@pytest.mark.parametrize("input_values, expected",
                         [(("23", "24", "25"), TypeError), (["2", "f"], TypeError)],
                         ids=['"23", "24", "25"', '["2", "f"]'])
def test_arithmetic_mean_negative(input_values, expected):
    with pytest.raises(TypeError):
        arithmetic_mean(input_values)
