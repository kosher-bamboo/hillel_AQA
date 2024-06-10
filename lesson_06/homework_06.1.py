# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()


value = input("Enter value:")
input_set = len(set(value))

print(input_set)

if input_set > 10:
    print(True)
else:
    print(False)
