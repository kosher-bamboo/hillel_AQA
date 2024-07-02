from lesson_07.homework_07 import even_number_sum


def test_even_number_sum_above_zero():
    assert even_number_sum(range(11)) == 30


def test_even_number_sum_below_zero():
    assert even_number_sum([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11]) == -30


def test_even_number_sum_zero():
    assert even_number_sum([]) == 0
