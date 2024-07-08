import pytest

from lesson_07.homework_07 import count_title_words

input_values = ("While the late steamer \"Big Missouri\" worked and sweated in the sun",
                "the retired artist sat on a barrel in the shade close by, dangled his legs, munched his apple,"
                "and planned the slaughter of more innocents",
                "THE RETIRED ARTIST SAT ON THE BARREL IN THE SHADE CLOSE BY, DANGLED HIS LEGS, "
                "MUNCHED HIS APPLE, AND PLANNED THE SLAUGHTER OF MORE INNOCENTS", "", "24"
                )
expected = (3, 0, 0, 0, 0)
zip_params = list(zip(input_values, expected))


@pytest.mark.positive
@pytest.mark.count_title_words
@pytest.mark.parametrize("input_values, expected", zip_params, ids=["01", "02", "03", "04", "05"])
def test_count_title_words_positive(input_values, expected):
    assert count_title_words(input_values) == expected
