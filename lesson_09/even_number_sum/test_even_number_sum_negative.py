import unittest

from lesson_07.homework_07 import even_number_sum


class EvenNumberSumNegativeTest(unittest.TestCase):

    def test_even_number_sum_string(self):

        input_value = ["1", "2", "3"]
        expected_result = "not all arguments converted during string formatting"

        with self.assertRaises(TypeError) as type_error:
            even_number_sum(input_value)
        error_message = type_error.exception.args[0]

        self.assertEqual(error_message, expected_result)


if __name__ == '__main__':
    unittest.main()
