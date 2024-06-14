# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
# (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".


char_h = 0
while char_h < 1:
    input_value = input("Enter something with char 'H' or 'h': ")
    if 'H' in input_value or 'h' in input_value:
        print("Great!")
        char_h = 1

