import pytest

from lesson_07.homework_07 import even_number_sum


@pytest.mark.negative
@pytest.mark.even_number_sum
def test_even_number_sum_string_negative():
    with pytest.raises(TypeError):
        even_number_sum(["1", "2", "3"])
