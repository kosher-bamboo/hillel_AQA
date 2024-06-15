# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
print("task 01")


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 10:
        result = number * multiplier
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)

# task 2 "Написати функцію, яка обчислює суму двох чисел."
print("\ntask 02")


def sum_of_numbers(a, b):
    return a + b


a = 12
b = 21
print(f"sum of numbers {a} and {b} is: {sum_of_numbers(12, 21)}")

# task 3 "Написати функцію, яка розрахує середнє арифметичне списку чисел."
print("\ntask 03")


def arithmetic_mean(*args):
    sum_of_args = 0

    # sum of all args
    for arg in args:
        sum_of_args += arg
    average = sum_of_args / len(args)
    return average


print(f"average of args is: {arithmetic_mean(2, 4, 6, 8, 9)}")

# task 4 "Написати функцію, яка приймає рядок та повертає його у зворотному порядку."
print("\ntask 04")


def reverce_string(standart_string):
    reverce_string = standart_string[::-1]
    return reverce_string


standart_string = "Написати функцію, яка приймає рядок та повертає його у зворотному порядку."
print(standart_string)
print(f"reverce string: {reverce_string(standart_string)}")


# task 5 "Написати функцію, яка приймає список слів та повертає найдовше слово у списку."
print("\ntask 05")


def longest_word(initial_string):

    # initialize new dict
    words_dict = {}
    words = set(initial_string.split())  # the set of unique words

    # fill the dict with words as keys and its length as values
    for word in words:
        words_dict[word] = len(word)

    # create a new dict with items sorted by the value (i.e. words length)
    sorted_words_dict = sorted(words_dict.items(), key=lambda x: x[1])
    return sorted_words_dict[-1][0]


initial_string = "Lorem Ipsum is simply dummy text of the printing and typesetting industry"
print(longest_word(initial_string))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
print("\ntask 06")


def find_substring(str1, str2):
    return str1.index(str2) if (str2 in str1) else -1


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

"""
Порахувати кількість унікальних символів в строці.
Якщо їх більше 10 - вивести в консоль True, інакше - False.
Строку отримати за допомогою функції input()
"""
print("\ntask 07")


def unique_symbols(input_value):

    # transform list to set for unique symbols and count it
    value_unique_length = len(set(input_value))

    # check the number of unique sumbols; True if > 10, Else is < 10
    return True if value_unique_length > 10 else False

input_value = "weiruyweiur"
print(unique_symbols(input_value))

input_value = "czmbn sdfkladj ewyruioweqy zxcvm,zb sadfasd"
print(unique_symbols(input_value))


# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
print("\ntask 08")


def even_number_sum(input_list):

    # initialize variable to sum even numbers
    even_numbers_sum = 0

    # found even numbers in the input range and sum it
    for element in input_list:
        if element%2 == 0:  # find evenly divided numbers
            even_numbers_sum += element  # sum evenly divided numbers
    return even_numbers_sum


print(f"even number sum is {even_number_sum(range(44))}")

# Виведіть, скільки слів у тексті починається з Великої літери?
print("\ntask 09")


def count_title_words(input_text):

    # initialize new list
    title_words_array = []

    # split input string into separate words
    for word in input_text.split():
        if word.istitle():  # check if word begins with a capital letter
            title_words_array.append(word)  # add such words in the list
    return len(title_words_array)

input_text = """Tom gave up the brush with reluctance in his face but alacrity in his heart. 
And while the late steamer "Big Missouri" worked and sweated in the sun, 
the retired artist sat on a barrel in the shade close by, dangled his legs, munched his apple, 
and planned the slaughter of more innocents. There was no lack of material; boys happened along every little while; 
they came to jeer, but remained to whitewash. 
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for a kite, in good repair; 
and when he played out, Johnny Miller bought in for a dead rat and a string to swing it with—and so on, and so on, 
hour after hour. And when the middle of the afternoon came, from being a poor poverty, stricken boy in the morning, 
Tom was literally rolling in wealth."""

print(f"there are {count_title_words(input_text)} words starts with a capital letter")

# Отримати на вході список значень і вивести тільки значення типу string
print("\ntask 10")


def string_only(initial_list):

    # initialize new list
    string_only_list = []

    for item in initial_list:
        if type(item) is str:  # check if item has string type
            string_only_list.append(item)  # add such items to the list
    return string_only_list

initial_list = [-94.79, 'vjqbxrguip', -58, '19', 60, 'True', True, '-43', 'okqnacfc', False, 43, 54, 40, 'bcx', 5,
          'qiqvcvwyln', True, 'zsqbqbmw', 'z', 'qcj']
print(string_only(initial_list))
