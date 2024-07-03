import pytest


from lesson_07.homework_07 import arithmetic_mean


@pytest.mark.positive
@pytest.mark.arithmetic_mean
class TestArithmeticMeanPositive:

    input_values_args = ((1, 2, 3, 4, 5), (-1, -2, -3))
    expected_args = (3, -2)
    zip_params_args = list(zip(input_values_args, expected_args))

    @pytest.mark.parametrize("input_values_args, expected_args", zip_params_args, ids=["1, 2, 3, 4, 5", "-1, -2, -3"])
    def test_arithmetic_mean_positive_0(self, input_values_args, expected_args):
        assert arithmetic_mean(*input_values_args) == expected_args

    input_values = (5, 0, -4)
    expected = (5, 0, -4)
    zip_params = list(zip(input_values, expected))

    @pytest.mark.parametrize("input_values, expected", zip_params, ids=input_values)
    def test_arithmetic_mean_positive_1(self, input_values, expected):
        assert arithmetic_mean(input_values) == expected
