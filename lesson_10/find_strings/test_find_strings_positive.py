import pytest

from lesson_09.functions import find_strings


input_values = ([-94.79, 'vjqbxrguip', -58], [-94.79, -58, 60, 43, 54, 40, 5], "")
expected = (['vjqbxrguip'], [], [])
zip_params = (list(zip(input_values, expected)))


@pytest.mark.positive
@pytest.mark.find_strings
@pytest.mark.parametrize("input_values, expected", zip_params, ids=["01", "02", "03"])
def test_find_strings_positive(input_values, expected):
    assert find_strings(input_values) == expected
