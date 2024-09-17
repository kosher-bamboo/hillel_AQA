import unittest
import allure

from lesson_07.homework_07 import arithmetic_mean

@allure.epic("Unit tests")
@allure.feature("Arithmetic Mean Tests")
@allure.story("Negative Tests")
class ArithmeticMeanNegativeTest(unittest.TestCase):

    @allure.title("Empty input")
    def test_arithmetic_mean_string(self):

        expected_result = "division by zero"

        with self.assertRaises(ZeroDivisionError) as error:
            arithmetic_mean()  # do not pass anything to the function
        result = error.exception.args[0]

        self.assertEqual(result, expected_result)

    @allure.title("Input: list")
    def test_arithmetic_mean_list(self):

        input_value = ["2", "f"]
        expected_result = "unsupported operand type(s) for +=: 'int' and 'list'"

        with self.assertRaises(TypeError) as type_error:
            arithmetic_mean(input_value)
        error_message = type_error.exception.args[0]

        self.assertEqual(error_message, expected_result)


# if __name__ == '__main__':
#     unittest.main()
