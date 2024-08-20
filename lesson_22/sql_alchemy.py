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
#
list_of_students = []

"""
Напишіть програму, яка додає нового студента до бази даних та додає його до певного курсу.
Переконайтеся, що ці зміни коректно відображаються у базі даних.
"""
student = StudentsTable(name=fake.name())
list_of_students.append(student.name)

# Select random course and check if it's already exists in DB. Otherwise create it.
random_course = fake.random_element(list_of_courses)
course = session.query(CoursesTable).filter_by(course_title=random_course).first()
if not course:
    course = CoursesTable(course_title=random_course)
    logging.info(f'Created course: {course.course_title}')

# create an association between student and course
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
               .filter(CoursesTable.course_title == random_course).all())

for item in db_students:
    print(f'{item.name} study on: {item.courses[0].course_title}')

"""
Напишіть запити до бази даних, які повертають інформацію про курси, на які зареєстрований певний студент.
"""
random_student_name = fake.random_element(list_of_students)
db_courses = (session.query(CoursesTable)
              .join(StudentsTable, CoursesTable.students)
              .filter(StudentsTable.name == random_student_name).all())
print(f'{random_student_name} study on:')
for item in db_courses:
    print(f'{item.course_title}')

"""
Реалізуйте можливість оновлення даних про студентів або курси, а також видалення студентів з бази даних.
"""
edit_students = session.query(StudentsTable).filter_by(name=random_student_name).all()
for student in edit_students:
    student.name = f'{random_student_name} Renamed'
session.commit()

# get an old course want to edit
old_course = session.query(CoursesTable).filter_by(course_title=random_course).first()

if old_course:
    # Create a new course with the new title
    new_course = session.query(CoursesTable).filter_by(course_title='Just another course 2').first()
    if new_course:
        print("Course already exists")
    else:
        new_course = CoursesTable(course_title='Just another course 2')
    session.add(new_course)

    # Move associations to the new course
    for student in old_course.students:
        student.courses.remove(old_course)
        student.courses.append(new_course)

    # Delete the old course
    session.delete(old_course)

    session.commit()

students_to_delete = session.query(StudentsTable).filter_by(name='David Gonzalez').first()
session.delete(student)
session.commit()
