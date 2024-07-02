import pytest

from lesson_07.homework_07 import even_number_sum


def test_even_number_sum_string():
    with pytest.raises(TypeError):
        even_number_sum(["1", "2", "3"])
