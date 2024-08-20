from sqlalchemy.orm import sessionmaker
from lesson_22.alchemy_base import engine, Base
from lesson_22.tables import StudentsTable, CoursesTable
from faker import Faker
import logging

logging.basicConfig(filename='students.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger()

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

"""
Напишіть програму, яка додає нового студента до бази даних та додає його до певного курсу.
Переконайтеся, що ці зміни коректно відображаються у базі даних.
"""
student = StudentsTable(name=fake.name())
course = CoursesTable(course_title=fake.random_element(list_of_courses))
student.courses.append(course)
session.add(student)
session.commit()
logging.info(f'Created student: {student.name}')

db_student_exist = session.query(StudentsTable).filter_by(name=student.name).first()
logging.info(f'Student from DB: {db_student_exist.name}')
assert student == db_student_exist

"""
Напишіть запити до бази даних, які повертають інформацію про студентів, зареєстрованих на певний курс
"""
db_students = (session.query(StudentsTable)
               .join(CoursesTable, StudentsTable.courses)
               .filter(CoursesTable.course_title == 'Just another course').all())

for item in db_students:
    print(f'{item.name} study at {item.courses[0].course_title}')

"""
Напишіть запити до бази даних, які повертають інформацію про курси, на які зареєстрований певний студент.
"""
students_name = 'Paul King'
db_courses = (session.query(CoursesTable)
              .join(StudentsTable, CoursesTable.students)
              .filter(StudentsTable.name == students_name).all())
print('Paul King studying on:')
for item in db_courses:
    print(f'{item.course_title}')

"""
Реалізуйте можливість оновлення даних про студентів або курси, а також видалення студентів з бази даних.
"""
edit_students = session.query(StudentsTable).filter_by(name='Paul King').all()
for student in edit_students:
    student.name = 'Paul King 2'
session.commit()

edit_courses = session.query(CoursesTable).filter_by(course_title='Human Anatomy and Physiology').all()
for course in edit_courses:
    course.course_title = 'Just another course'
session.commit()

students_to_delete = session.query(StudentsTable).filter_by(name='Paul King 2').all()
for student in students_to_delete:
    session.delete(student)
session.commit()
