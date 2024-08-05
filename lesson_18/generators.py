print("Напишіть генератор, який повертає послідовність парних чисел від 0 до N.")
from lesson_18.decorators import log_args_and_result

even_numbers_generator = (x for x in range(10) if x % 2 == 0)

for number in even_numbers_generator:
    print(number)

print("-" * 10)

print("генератор, який повертає послідовність парних чисел від 0 до N у вигляді функції")


@log_args_and_result
def even_numbers_generator(numbers):
    for x in range(numbers):
        if x % 2 == 0:
            yield x


for num in even_numbers_generator(10):
    print(num)

print("-" * 10)

print("Створіть генератор, який генерує послідовність Фібоначчі до певного числа N")


@log_args_and_result
def fibonacci_generator(number):
    a, b = 0, 1
    while a < number:
        yield a
        a, b = b, a + b


for num in fibonacci_generator(10):
    print(num)
