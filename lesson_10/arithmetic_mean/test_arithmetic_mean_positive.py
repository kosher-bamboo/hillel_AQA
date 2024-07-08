import pytest


from lesson_07.homework_07 import arithmetic_mean


@pytest.mark.positive
@pytest.mark.arithmetic_mean
class TestArithmeticMeanPositive:

    input_values = ((1, 2, 3, 4, 5), (-1, -2, -3), (5,), (0,), (-4,))
    expected = (3, -2, 5, 0, -4)
    zip_params = list(zip(input_values, expected))

    @pytest.mark.parametrize("input_values_args, expected_args", zip_params,
                             ids=["1, 2, 3, 4, 5", "-1, -2, -3", "5", "0", "-4"])
    def test_arithmetic_mean_positive_0(self, input_values_args, expected_args):
        assert arithmetic_mean(*input_values_args) == expected_args
