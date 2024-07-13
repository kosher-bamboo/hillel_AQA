"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента.
Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
Виведіть інформацію про студента та змініть його середній бал.
"""


class Student:
    #
    def __init__(self, first_name, second_name, age, average_grade):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.average_grade = average_grade

    def update_average_grade(self, updated_average_grade):
        self.average_grade = updated_average_grade


student_1 = Student(first_name="John", second_name="Doe", age="30", average_grade=80)
print(f"Student {student_1.first_name} {student_1.second_name} is {student_1.age}. "
      f"His average grade is {student_1.average_grade}")

student_1.update_average_grade(90)

print(f"Student {student_1.first_name} {student_1.second_name} is {student_1.age}. "
      f"His average grade is {student_1.average_grade}")
