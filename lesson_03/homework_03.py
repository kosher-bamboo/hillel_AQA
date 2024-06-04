alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where ——" said Alice.\n'
                       '"Then it doesn\'t matter which way you go," said the Cat.\n"'
                       '—— so long as I get somewhere," Alice added as an explanation.\n"'
                       'Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."\n')

print("task 01-03")
print(alice_in_wonderland)

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
#     # зрозуміло дитині, що навчається в п'ятому класі
# """

# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

print(f"task 04")
sqare_black_sea = 436402
sqare_azov_sea = 37800
sqare_all = sqare_black_sea + sqare_azov_sea
print(f"Загальна площа Чорного та Азовського морів становить {sqare_all} км2")

# task 05
"""
# Мережа супермаркетів має 3 склади, де всього розміщено
# 375 291 товар. На першому та другому складах перебуває
# 250 449 товарів. На другому та третьому – 222 950 товарів.
# Знайдіть кількість товарів, що розміщені на кожному складі.
"""
print("task 05")
warehouse_all = 375291
warehouse_01_02 = 250449
warehouse_02_03 = 222950
warehouse_01 = warehouse_all - warehouse_02_03
warehouse_03 = warehouse_all - warehouse_01_02
warehouse_02 = warehouse_all - warehouse_01 - warehouse_03
print(f"На першому складі {warehouse_01} товарів, на другому - {warehouse_02} товарів, на третьому - {warehouse_03} товарів.")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
print("task 06")
price_per_month = 1179
months = 18
total_price = price_per_month * months
print(f"Вартість компьютера складатиме {total_price} грн")


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print("task 07")
number_a = 8019
divisor_a = 8
number_b = 9907
divisor_b = 9
number_c = 2789
divisor_c = 5
number_d = 7248
divisor_d = 6
number_e = 7128
divisor_e = 5
number_f = 19224
divisor_f = 9

division_a = number_a / divisor_a
remainder_a = division_a - int(division_a)
division_b = number_b / divisor_b
remainder_b = division_b - int(division_b)
division_c = number_c / divisor_c
remainder_c = division_c - int(division_c)
division_d = number_d / divisor_d
remainder_d = division_d - int(division_d)
division_e = number_e / divisor_e
remainder_e = division_e - int(division_e)
division_f = number_f / divisor_f
remainder_f = division_f - int(division_f)

print(f"Остача від ділення:\n"
      f"8019 на 8 становить {remainder_a},\n"
      f"9907 на 9 становить {remainder_b},\n"
      f"2789 на 5 становить {remainder_c},\n"
      f"7248 на 6 становить {remainder_d},\n"
      f"7128 на 5 становить {remainder_e},\n"
      f"19224 на 9 становить {remainder_f}.\n")


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
print("task 08")
large_pizza_price = 274
large_pizza_number = 4
medium_pizza_price = 218
medium_pizza_number = 2
juice_price = 35
juice_number = 4
cake_price = 350
cake_number = 1
water_price = 21
water_number = 3
checkout = ((large_pizza_price * large_pizza_number) + (medium_pizza_price * medium_pizza_number)
            + (juice_price * juice_number) + (cake_price * cake_number) + (water_price * water_number))
print(f"Для замовлення знадобиться {checkout} грн")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
print("task 09")
photos = 232
photos_per_page = 8
total_pages = round(photos / photos_per_page)
print(f"Всього знадобиться {total_pages} сторінок")


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
print("task 10")
distance = 1600
gasoline_consumption = 9
tank_volume = 48
total_gasoline_consumption = round(distance / gasoline_consumption, 1)
print(f"Всього знадобиться {total_gasoline_consumption} літрів бензину")

full_tank_distance = tank_volume / gasoline_consumption * 100
refuel_number = round(distance / full_tank_distance)
# print(full_tank_distance)
print(f"Знадобиться заїхати на заправку щонайменше {refuel_number} рази(ів)")
