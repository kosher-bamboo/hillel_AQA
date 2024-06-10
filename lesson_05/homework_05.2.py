# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
    ('John', 'Doe', 28, 'Engineer', 'New York'),
    ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
    ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
    ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
    ('Michael', 'Brown', 22, 'Student', 'Seattle'),
    ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
    ('David', 'Miller', 33, 'Software Developer', 'Austin'),
    ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
    ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
    ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
    ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
    ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
    ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
    ('Ava', 'White', 42, 'Journalist', 'San Diego'),
    ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

people_records.insert(0, ('Oleksandr', 'Marar', 31, 'Engineer', 'Odesa'))
print(f"#1. Updated list: {people_records}")


index_5 = people_records.pop(5)
index_1 = people_records.pop(1)
people_records.insert(1, index_5)
people_records.insert(5, index_1)
print(f"\n#2. Swapped items 1 and 5: {people_records}")


print("\n#3. ")
# 3 - check that all people in modified list with records indexes 6, 10, 13 have age >=30. Print condition check result
if int(people_records[6][2]) >= 30:
    print(f"{people_records[6][0]} {people_records[6][1]}'s age is >= 30. It's {people_records[6][2]}")
if int(people_records[10][2]) >= 30:
    print(f"{people_records[10][0]} {people_records[10][1]}'s age is >= 30. It's {people_records[10][2]}")
if int(people_records[13][2]) >= 30:
    print(f"{people_records[13][0]} {people_records[13][1]}'s age is >= 30. It's {people_records[13][2]}")
