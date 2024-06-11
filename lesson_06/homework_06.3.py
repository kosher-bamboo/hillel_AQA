# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
# Данні в лісті можуть бути будь якими

list_1 = [-94.79, 'vjqbxrguip', -58, '19', 60, 'True', True, '-43', 'okqnacfc', False, 43, 54, 40, 'bcx', 5,
          'qiqvcvwyln', True, 'zsqbqbmw', 'z', 'qcj']
list_2 = []

for item in list_1:
    if type(item) is str:
        list_2.append(item)
print(list_2)
