from sqlalchemy.orm import sessionmaker
from lesson_22.alchemy_base import engine, Base
from lesson_22.tables import StudentsTable, CoursesTable
from faker import Faker
import logging

logging.basicConfig(filename='hb_test.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fake = Faker()

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

list_of_courses = [
    "Introduction to Psychology",
    "Calculus I",
    "World History: Ancient Civilizations",
    "Principles of Economics",
    "Organic Chemistry",
    "Introduction to Computer Science",
    "English Literature: Shakespeare",
    "Environmental Science",
    "Digital Marketing Fundamentals",
    "Human Anatomy and Physiology"
]

# list of courses
# introduction_to_psychology = CoursesTable(course_title="Introduction to Psychology")
# calculus_i = CoursesTable(course_title="Calculus I")
# ancient_civilizations = CoursesTable(course_title="World History: Ancient Civilizations")
# principles_of_economics = CoursesTable(course_title="Principles of Economics")
# organic_chemistry = CoursesTable(course_title="Organic Chemistry")
# introduction_to_computer_science = CoursesTable(course_title="Introduction to Computer Science")
# english_literature_shakespeare = CoursesTable(course_title="English Literature: Shakespeare")
# environmental_science = CoursesTable(course_title="Environmental Science")
# digital_marketing_fundamentals = CoursesTable(course_title="Digital Marketing Fundamentals")
# human_anatomy_and_physiology = CoursesTable(course_title="Human Anatomy and Physiology")
#
# list_of_courses_ = [introduction_to_psychology, calculus_i, ancient_civilizations, principles_of_economics,
#                    organic_chemistry, introduction_to_computer_science, english_literature_shakespeare,
#                    environmental_science, digital_marketing_fundamentals, human_anatomy_and_physiology]

#
# list_of_students_with_courses = [
#     {"name": "Emma Thompson", "course": introduction_to_psychology},
#     {"name": "Liam Chen", "course": calculus_i},
#     {"name": "Sophia Rodriguez", "course": ancient_civilizations},
#     {"name": "Noah Patel", "course": principles_of_economics},
#     {"name": "Emma Thompson", "course": organic_chemistry},
#     {"name": "Ethan Nguyen", "course": introduction_to_computer_science},
#     {"name": "Ava Johnson", "course": english_literature_shakespeare},
#     {"name": "Mason Williams", "course": environmental_science},
#     {"name": "Isabella Garcia", "course": digital_marketing_fundamentals},
#     {"name": "William Lee", "course": human_anatomy_and_physiology},
#     {"name": "Mia Anderson", "course": introduction_to_psychology},
#     {"name": "James Taylor", "course": calculus_i},
#     {"name": "Charlotte Brown", "course": ancient_civilizations},
#     {"name": "Benjamin Moore", "course": principles_of_economics},
#     {"name": "Amelia Davis", "course": organic_chemistry},
#     {"name": "Emma Thompson", "course": introduction_to_computer_science},
#     {"name": "Harper Martinez", "course": english_literature_shakespeare},
#     {"name": "Alexander White", "course": environmental_science},
#     {"name": "Evelyn Scott", "course": digital_marketing_fundamentals},
#     {"name": "Daniel Jackson", "course": human_anatomy_and_physiology},
#     {"name": "Abigail Lewis", "course": introduction_to_psychology},
#     {"name": "Michael Robinson", "course": calculus_i},
#     {"name": "Emily Clark", "course": ancient_civilizations},
#     {"name": "David Miller", "course": principles_of_economics},
#     {"name": "Elizabeth Hall", "course": organic_chemistry},
#     {"name": "Joseph Young", "course": introduction_to_computer_science},
#     {"name": "Sofia Adams", "course": english_literature_shakespeare},
#     {"name": "Christopher Allen", "course": environmental_science},
#     {"name": "Grace Turner", "course": digital_marketing_fundamentals},
#     {"name": "Matthew Harris", "course": human_anatomy_and_physiology},
#     {"name": "Chloe Baker", "course": introduction_to_psychology},
#     {"name": "Andrew King", "course": calculus_i},
#     {"name": "Zoe Wright", "course": ancient_civilizations},
#     {"name": "Ryan Lopez", "course": principles_of_economics},
#     {"name": "Lily Green", "course": organic_chemistry},
#     {"name": "Joshua Phillips", "course": introduction_to_computer_science},
#     {"name": "Layla Campbell", "course": english_literature_shakespeare},
#     {"name": "Samuel Evans", "course": environmental_science},
#     {"name": "Aria Mitchell", "course": digital_marketing_fundamentals},
#     {"name": "Nathan Carter", "course": human_anatomy_and_physiology},
#     {"name": "Audrey Ross", "course": introduction_to_psychology},
#     {"name": "Tyler Cooper", "course": calculus_i},
#     {"name": "Scarlett Reed", "course": ancient_civilizations},
#     {"name": "Dylan Murphy", "course": principles_of_economics},
#     {"name": "Hannah Cook", "course": organic_chemistry},
#     {"name": "Isaac Bennett", "course": introduction_to_computer_science},
#     {"name": "Leah Morgan", "course": english_literature_shakespeare},
#     {"name": "Owen Foster", "course": environmental_science},
#     {"name": "Zoe Peterson", "course": digital_marketing_fundamentals},
#     {"name": "Caleb Rivera", "course": human_anatomy_and_physiology}
# ]

list_of_students = [
'Ryan Chen',
'Shawn Martinez',
'Tiffany Yang',
'Kayla Campbell',
'Jason Garcia',
'Steven Sheppard',
'Sheryl Shaw',
'Meredith Wolf',
'Thomas Vasquez',
'Deborah Hernandez',
'Ryan Bell',
'Mark Griffith',
'Tina Bond',
'Bryan Grant',
'Christina Silva',
'Gina Pruitt',
'Ryan Simpson',
'Amy Mathews',
'Jason Smith',
'Justin Pacheco',
'Richard Richard',
'Beverly Daniel',
'Alicia Mcneil',
'Nancy Diaz',
'Jeff Terry',
'Adriana Brown',
'Scott Miller',
'Dylan Chang',
'Albert Jackson',
'Johnny Alvarado',
'Matthew Dyer',
'Brent Watson',
'Holly Good',
'April Hill',
'Donald Wright',
'Lisa Woodward',
'Jamie Peters',
'Debra Shaw',
'Benjamin Zavala',
'Cynthia Burke',
'Mary Vazquez',
'Brenda Kane',
'Kimberly Henderson',
'Matthew Evans',
'Jennifer Lamb',
'Jennifer Anderson',
'Clinton Sheppard',
'Sydney Brooks',
'Brad Acosta DDS',
'Jeffrey Perkins'
]

# add students and courses tables
# students_to_add = [StudentsTable(**student) for student in list_of_students_with_courses]
# session.add_all(list_of_students)
# session.commit()

"""
Напишіть програму, яка додає нового студента до бази даних та додає його до певного курсу.
Переконайтеся, що ці зміни коректно відображаються у базі даних.
"""
student = StudentsTable(name=fake.name())
course = CoursesTable(course_title=fake.random_element(list_of_courses))
student.course.append(course)
session.add(student)
session.commit()

# db_student_exist = session.query(StudentsTable).filter_by(name=student.name).first()
# assert student == db_student_exist

"""
Напишіть запити до бази даних, які повертають інформацію про студентів, зареєстрованих на певний курс
"""
db_courses = (session.query(StudentsTable)
              .join(CoursesTable, StudentsTable.courses)
              .filter(CoursesTable.course_title == 'Introduction to Psychology').all())

for item in db_courses:
    print(f'{item.name} study at {item.courses[0].course_title}')

# db_course = session.query(StudentsTable).join(CoursesTable).filter(CoursesTable.course_title == 'Organic Chemistry').all()
# for item in db_course:
#     print(f'{item.name} study at {item.course.course_title}')

"""
Напишіть запити до бази даних, які повертають інформацію про курси, на які зареєстрований певний студент.
"""
# db_courses = (session.query(CoursesTable)
#               .join(StudentsTable, CoursesTable.name)
#               .filter(StudentsTable.name == 'April Hill').all())

# for item in db_courses:
#     print(f'{item.students[0].name} study at {item.course_title}')

# db_student = session.query(StudentsTable).join(CoursesTable).filter(StudentsTable.name == 'Emma Thompson').all()
# for item in db_student:
#     print(f'{item.name} study at {item.course.course_title}')

"""
Реалізуйте можливість оновлення даних про студентів або курси, а також видалення студентів з бази даних.
"""
# students = session.query(StudentsTable).filter_by(name='Emma Thompson').all()
# for student in students:
#     student.name = 'Emma Thompson 2'
# session.commit()


# courses = session.query(CoursesTable).filter_by(course_title='Human Anatomy and Physiology').all()
# for course in courses:
#     course.course_title = 'Just another course'
# session.commit()

# students = session.query(StudentsTable).filter_by(name='Emma Thompson 2').all()
# for student in students:
#     session.delete(student)
# session.commit()
