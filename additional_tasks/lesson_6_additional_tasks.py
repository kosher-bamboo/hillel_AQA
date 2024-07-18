"""
1 - Є 3 группи людей(sets) australia_blacklist, poker_blacklist, alcohol_blacklist.
В кожній групі вказані імена. Вивести тих хто виграв джекпот(є одразу в 3х списках)
"""

australia_blacklist = ["Emma", "Noah", "Olivia", "Liam", "Ava", "Ethan", "Sophia", "Mason", "Isabella", "William", "Mia", "James"]

poker_blacklist = ["Sophia", "Jackson", "Emma", "Aiden", "Noah", "Lucas", "Harper", "Elijah", "Amelia", "Oliver", "Evelyn", "Benjamin"]

alcohol_blacklist = ["Charlotte", "Noah", "Abigail", "Emma", "Michael", "Emily", "Alexander", "Madison", "Daniel", "Elizabeth", "David", "Avery"]

common_names = {name for name in australia_blacklist if name in poker_blacklist and name in alcohol_blacklist}
print(common_names)

"""
2 - Порахувати та вивести(print) кількість букв в строці.
Юзер щось вводить(input)
Ваша задача надрукувати кількість кожного символу того що він ввів.
Прикдад:
Юзер вводить: My name is Emmy Santiago.
Ви прінтаете щось накшталт:
M = 1, y = 2, n = 2, ...(або в іншому форматі, це не принципово, головне, що б чітко було зрозуміло скільки разів зустрічаеться кожна буква)
Тобто кожну букву та скільки разів вона зустрічаеться

Підказка: це про словники, get можна використати для тотго щоб витягнути чи є ключ без помилки та надати дефолтне значення
"""

# user_input = input()
user_input = "My name is Emmy Santiago"

new_dict = {x: user_input.count(x) for x in user_input}

print(new_dict)

"""
3 - Вирішити задачу 2 без словника за 2 строки:
1 строка це input
2 строка це рішення
"""

user_input = "My name is Emmy Santiago"
new_set = {f"{x} = {user_input.count(x)}" for x in user_input}

print(new_set)
