import unittest

from lesson_09.functions import find_strings


class FindStringsPositiveTest(unittest.TestCase):
    def test_find_strings(self):

        input_value = [-94.79, 'vjqbxrguip', -58]
        expected_result = ['vjqbxrguip']

        self.assertEqual(find_strings(input_value), expected_result)

    def test_find_strings_numbers(self):

        input_value = [-94.79, -58, 60, 43, 54, 40, 5]
        expected_result = []

        self.assertEqual(find_strings(input_value), expected_result)

    def test_find_strings_empty(self):

        input_value = []
        expected_result = []

        self.assertEqual(find_strings(input_value), expected_result)
