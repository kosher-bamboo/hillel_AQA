import unittest

from lesson_09.functions import find_strings


class FindStringsNegativeTest(unittest.TestCase):
    def test_find_strings_None(self):

        input_value = None
        expected_result = "'NoneType' object is not iterable"

        with self.assertRaises(TypeError) as error:
            find_strings(input_value)
        error_message = error.exception.args[0]

        self.assertEqual(error_message, expected_result)

    def test_find_strings_number(self):

        input_value = 24
        expected_result = "'int' object is not iterable"

        with self.assertRaises(TypeError) as error:
            find_strings(input_value)
        error_message = error.exception.args[0]

        self.assertEqual(error_message, expected_result)
