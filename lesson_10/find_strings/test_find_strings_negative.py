import pytest

from lesson_09.functions import find_strings


input_values = (None, 24)
expected = (TypeError, TypeError)
zip_params = (list(zip(input_values, expected)))


@pytest.mark.negative
@pytest.mark.find_strings
@pytest.mark.parametrize("input_values, expected", zip_params, ids=input_values)
def test_find_strings_negative(input_values, expected):
    with pytest.raises(TypeError):
        find_strings(input_values)
