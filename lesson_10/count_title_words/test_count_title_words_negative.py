import pytest

from lesson_07.homework_07 import count_title_words

input_values = ((24, 25), ["Word", "word"])
expected = (AttributeError, AttributeError)


@pytest.mark.negative
@pytest.mark.count_title_words
@pytest.mark.parametrize("input_values, expected", [((24, 25), AttributeError), (["Word", "word"], AttributeError)],
                         ids=["24, 25", '"Word", "word"'])
def test_count_title_words_negative(input_values, expected):
    with pytest.raises(AttributeError):
        count_title_words(input_values)
