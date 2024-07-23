"""
Напишіть інтерактивний калькулятор. Передбачається, що користувач вводить формулу, що складається з числа,
оператора (як мінімум * і /) та іншого числа, розділених пробілом (наприклад, 2 * 5).
Якщо вхідні дані не складаються з трьох елементів, генеруйте та спіймайте власний ексепшн FormulaError.
Якщо другий елемент не є «*» або «/», генеруйте та спіймайте власний ексепшн WrongOperatorError
Якщо введені числа не можуть бути float спіймайте ValueError
Також ловіть помилку при діленні на 0
В кожній спійманій помилці друкуйте пояснення, що пішло не так
Надайте три спроби скористуватись калькулятором, якщо введені не вірні дані, якщо не вийшло -
прінтайте що закінчились спроби
Результат виконання формули - float число з двома знаками після крапки
"""


class FormulaError(Exception):
    def __init__(self, message="there must be two operands and one operator"):
        self.message = message
        super().__init__(self.message)


class WrongOperatorError(Exception):
    def __init__(self, message="only '*' and '/' operators accepted"):
        self.message = message
        super().__init__(message)


def calculator():
    attempt = 0
    while attempt < 3:
        input_prompt_splited = input("calculate: ").split()
        try:
            if len(input_prompt_splited) != 3:  # check operands and operator
                raise FormulaError()
            if input_prompt_splited[1] not in ("*", "/"):
                raise WrongOperatorError()

            operand_1 = float(input_prompt_splited[0])
            operator = input_prompt_splited[1]
            operand_2 = float(input_prompt_splited[2])

            if operator == '*':
                return round(operand_1 * operand_2, 2)
            if operator == '/':
                return round(operand_1 / operand_2, 2)

        except FormulaError as fe:
            print(f"FormulaError: {fe}")
        except WrongOperatorError as woe:
            print(f"WrongOperatorError: {woe}")
        except ValueError:
            print(f"ValueError: use numbers only")
        except ZeroDivisionError:
            print(f"ZeroDivisionError: can't divide by zero")

        attempt += 1
