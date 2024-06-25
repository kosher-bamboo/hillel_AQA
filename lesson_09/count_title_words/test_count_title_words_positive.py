import unittest

from lesson_07.homework_07 import count_title_words


class CountTitleWordsPositiveTest(unittest.TestCase):

    def test_count_title_words(self):

        input_value =  "While the late steamer \"Big Missouri\" worked and sweated in the sun"
        expected_result = 3

        self.assertEqual(count_title_words(input_value), expected_result)

    def test_count_title_words_all_lower(self):

        input_value = ("the retired artist sat on a barrel in the shade close by, dangled his legs, munched his apple,"
                       "and planned the slaughter of more innocents")
        expected_result = 0

        self.assertEqual(count_title_words(input_value), expected_result)

    def test_count_title_words_all_apper(self):

        input_value = ("THE RETIRED ARTIST SAT ON THE BARREL IN THE SHADE CLOSE BY, DANGLED HIS LEGS, "
                       "MUNCHED HIS APPLE, AND PLANNED THE SLAUGHTER OF MORE INNOCENTS")
        expected_result = 0

        self.assertEqual(count_title_words(input_value), expected_result)

    def test_count_title_words_empty(self):

        input_value = ""
        expected_result = 0

        self.assertEqual(count_title_words(input_value), expected_result)

    def test_count_title_words_number(self):

        input_value = "24"
        expected_result = 0

        self.assertEqual(count_title_words(input_value), expected_result)


if __name__ == '__main__':
    unittest.main()
