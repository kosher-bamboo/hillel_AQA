import unittest

from lesson_07.homework_07 import count_title_words


class CountTitleWordsNegativeTest(unittest.TestCase):

    def test_count_title_words_list(self):

        input_value = ["Word", "word"]
        expected_result = "'list' object has no attribute 'split'"

        with self.assertRaises(AttributeError) as error:
            count_title_words(input_value)

        error_message = error.exception.args[0]
        # pass
        self.assertEqual(error_message, expected_result)

    def test_count_title_words_tuple(self):

        input_value = 24, 25
        expected_result = "'tuple' object has no attribute 'split'"

        with self.assertRaises(AttributeError) as error:
            count_title_words(input_value)

        error_message = error.exception.args[0]
        # pass
        self.assertEqual(error_message, expected_result)


if __name__ == '__main__':
    unittest.main()
