import pytest

from lesson_09.functions import find_strings


def test_find_strings_none():
    with pytest.raises(TypeError):
        find_strings(None)


def test_find_strings_number():
    with pytest.raises(TypeError):
        find_strings(24)
