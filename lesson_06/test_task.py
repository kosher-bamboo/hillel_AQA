"""
Умова: Написати програму, яка розраховує оподаткування на основі річного доходу користувача.

Отримайте річний дохід користувача.
Ми припускаємо, що користувач ЗАВЖДИ буде вводити нормальне число (≥0)
На основі введеного доходу розрахуйте податок за такими умовами:

Якщо дохід менше 10 000 грн, податок складає 10% від доходу.
Якщо дохід від 10 000 до 50 000 грн, податок складає 15% від доходу.
Якщо дохід більше 50 000 грн, податок складає 20% від доходу.

Запишіть результат у змінну tax_amount.
"""

# def calculate_tax(user_income):
#     if user_income < 10000:
#         tax_amount = user_income*0.1
#     elif user_income < 50000:
#         tax_amount = user_income*0.15
#     else: tax_amount = user_income*0.2
#
#     return tax_amount
#
# user_income = 5500
# print(f" {user_income}: {calculate_tax(user_income)}")
# user_income = 10000
# print(f" {user_income}: {calculate_tax(user_income)}")
# user_income = 20000
# print(f" {user_income}: {calculate_tax(user_income)}")
# user_income = 50000
# print(f" {user_income}: {calculate_tax(user_income)}")
# user_income = 70000
# print(f" {user_income}: {calculate_tax(user_income)}")


"""
Умова:
Ваша задача - написати функцію, яка визначає, чи є введене користувачем число простим чи складеним. 
Зазначте, що користувач завжди буде вводити цілі числа.
Простим вважаємо число, яке має 2 дільники - одиницю і саме це число
Ваш код повинен використовувати цикл та умови для визначення простоти числа.
Запишіть результат в змінну result.
"""


def is_prime_number(number):
    tsila_chastka = 0
    i = 1
    temp_list = []

    while tsila_chastka != 1:  # поки остача не стане = 1

        # число 2 при ділення на 1 і на 2 дає залишок 0, тому список буде містити два значення,
        # що за логікою програми означатиме складне число. Типу виключення :)
        if number == 2:
            return True
        else:
            tsila_chastka = number // i  # повертає цілу частку
            zalyshok = number % i  # повертає залишок від ділення
            if zalyshok == 0:
                temp_list.append(zalyshok)  # складаємо список з випадків, коли залишок = 0
            i += 1

    if len(temp_list) > 1:  # для складного числа випадків, коли залишок від ділення = 0, буде більше ніж 1
        return False
    else:  # для простого числа не буде випадків, коли залишок від ділення = 0
        return True


simple_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

for number in simple_numbers:
    print(is_prime_number(number))
