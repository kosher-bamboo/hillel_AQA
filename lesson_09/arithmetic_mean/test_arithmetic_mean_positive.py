import unittest
import allure

from lesson_07.homework_07 import arithmetic_mean

allure.epic("Unit tests")
allure.feature("Arithmetic Mean Tests")
allure.story("Positive Tests")
class ArithmeticMeanPositiveTest(unittest.TestCase):

    @allure.title("Input: 1 to 5")
    def test_arithmetic_mean_1_to_5(self):

        expected_result = 3

        self.assertEqual(arithmetic_mean(1, 2, 3, 4, 5), expected_result)

    @allure.title("Input: 5")
    def test_arithmetic_mean_5(self):

        input_value = 5
        expected_result = 5

        self.assertEqual(arithmetic_mean(input_value), expected_result)

    @allure.title("Input: 0")
    def test_arithmetic_mean_0(self):

        input_value = 0
        expected_result = 0

        self.assertEqual(arithmetic_mean(input_value), expected_result)

    @allure.title("Input: -4")
    def test_arithmetic_mean_minus_4(self):

        input_value = -4
        expected_result = -4

        self.assertEqual(arithmetic_mean(input_value), expected_result)

    @allure.title("Input: -1 to -3")
    def test_arithmetic_mean_minus_1_to_3(self):

        expected_result = -2

        self.assertEqual(arithmetic_mean(-1, -2, -3), expected_result)


# if __name__ == '__main__':
#     unittest.main()
