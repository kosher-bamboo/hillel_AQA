# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
# (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

# input_value = input("Enter something with char 'h':")
input_value = "sdfdafasHh"
unique_chars_set = set(input_value)
print(unique_chars_set)
print(len(unique_chars_set))

chars = 0
# while len(unique_chars_set)
for char in unique_chars_set:
    if char == 'H' or char == 'h':
        print("success")
