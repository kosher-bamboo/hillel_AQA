import unittest

from lesson_07.homework_07 import even_number_sum


class EvenNumberSumPositiveTest(unittest.TestCase):

    def test_even_number_sum_above_zero(self):

        input_value = range(11)
        expected_result = 30

        self.assertEqual(even_number_sum(input_value), expected_result)

    def test_even_number_sum_below_zero(self):

        input_value = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11]
        expected_result = -30

        self.assertEqual(even_number_sum(input_value), expected_result)

    def test_even_number_sum_zero(self):

        input_value = []
        expected_result = 0

        self.assertEqual(even_number_sum(input_value), expected_result)


if __name__ == '__main__':
    unittest.main()
