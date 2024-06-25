import unittest

from lesson_08.homework_08 import sum_all_number


class SumAllNumberPositiveTest(unittest.TestCase):

    def sum_all_number(self):
        input_value = ["1,2,3,4", "1,2,3,4,50"]
        expected_result = 3
        self.assertEqual(sum_all_number(input_value), expected_result)

if __name__ == '__main__':
    unittest.main()