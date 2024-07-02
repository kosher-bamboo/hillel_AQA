from lesson_09.functions import find_strings


def test_find_strings():
    assert find_strings([-94.79, 'vjqbxrguip', -58]) == ['vjqbxrguip']


def test_find_strings_numbers():
    assert find_strings([-94.79, -58, 60, 43, 54, 40, 5]) == []


def test_find_strings_empty():
    assert find_strings([]) == []
