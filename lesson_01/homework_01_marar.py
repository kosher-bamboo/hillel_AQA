# task 01 == Виправте синтаксичні помилки
print("Task 01")
print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки
print("Task 02")
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
print("Task 03")
for letter in "Hello world!":
         print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
print("Task 04")
apples = 2
banana = apples * 4
print("apples: " + str(apples))
print("banana: " + str(banana))

# task 05 == виправте назви змінних
print("Task 05")
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4
print(storona_1, storona_2, storona_3, storona_4, sep=", ")

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
print("Task 06")
perimeter = storona_1 + storona_2 + storona_3 + storona_4
print(f"perimeter: {perimeter}")


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
print("Task 07")
apple_tree = 4
pear_tree = apple_tree + 5
plum_tree = apple_tree - 2
all_trees = apple_tree + pear_tree + plum_tree
print(f"всього дерев: {all_trees}")

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
print("Task 08")
morning_temp = 5
day_temp = morning_temp - 10
evening_temp = day_temp + 4
print(f"температура надвечір: {evening_temp}")


# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
print("Task 09")
boys = 24
girls = round(boys / 2)
boys_sick = 1
girls_absent = 2
all_kids = boys - boys_sick + girls - girls_absent
print(f"у театральному гуртку {all_kids} дитини")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
print("Task 10")
book_1 = 8
book_2 = book_1 + 2
book_3 = (book_1 + book_2)/2
cost = book_1 + book_2 + book_3
cost = round(cost)
print(f"усі книги будуть коштувати {cost} грн.")