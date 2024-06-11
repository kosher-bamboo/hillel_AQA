# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

list_01 = list(range(17))
print(list_01)
even_numbers_sum = 0
for element in list_01:
    if element%2 == 0:
        even_numbers_sum += element
print(even_numbers_sum)
