from sqlalchemy.orm import sessionmaker
from lesson_22.alchemy_base import engine, Base
from lesson_22.tables.students_table import StudentsTable
from lesson_22.tables.courses_table import CoursesTable
from faker import Faker

fake = Faker()

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# list of courses
introduction_to_psychology = CoursesTable(course_title="Introduction to Psychology")
calculus_i = CoursesTable(course_title="Calculus I")
ancient_civilizations = CoursesTable(course_title="World History: Ancient Civilizations")
principles_of_economics = CoursesTable(course_title="Principles of Economics")
organic_chemistry = CoursesTable(course_title="Organic Chemistry")
introduction_to_computer_science = CoursesTable(course_title="Introduction to Computer Science")
english_literature_shakespeare = CoursesTable(course_title="English Literature: Shakespeare")
environmental_science = CoursesTable(course_title="Environmental Science")
digital_marketing_fundamentals = CoursesTable(course_title="Digital Marketing Fundamentals")
human_anatomy_and_physiology = CoursesTable(course_title="Human Anatomy and Physiology")

list_of_courses = [introduction_to_psychology, calculus_i, ancient_civilizations, principles_of_economics,
                   organic_chemistry, introduction_to_computer_science, english_literature_shakespeare,
                   environmental_science, digital_marketing_fundamentals, human_anatomy_and_physiology]


# list_of_courses = [
#     {"course_title": "Introduction to Psychology"},
#     {"course_title": "Calculus I"},
#     {"course_title": "World History: Ancient Civilizations"},
#     {"course_title": "Principles of Economics"},
#     {"course_title": "Organic Chemistry"},
#     {"course_title": "Introduction to Computer Science"},
#     {"course_title": "English Literature: Shakespeare"},
#     {"course_title": "Environmental Science"},
#     {"course_title": "Digital Marketing Fundamentals"},
#     {"course_title": "Human Anatomy and Physiology"},
# ]

# courses_to_add = [CoursesTable(**course) for course in list_of_courses]
# session.add_all([introduction_to_psychology,
#                  calculus_i,
#                  ancient_civilizations,
#                  principles_of_economics,
#                  organic_chemistry,
#                  introduction_to_computer_science,
#                  english_literature_shakespeare,
#                  environmental_science,
#                  digital_marketing_fundamentals,
#                  human_anatomy_and_physiology])
# session.commit()
#
# students_to_add_depr = [
# {"first_name": "Emma", "last_name": "Thompson"},
# {"first_name": "Liam", "last_name": "Chen"},
# {"first_name": "Sophia", "last_name": "Rodriguez"},
# {"first_name": "Noah", "last_name": "Patel"},
# {"first_name": "Olivia", "last_name": "Kim"},
# {"first_name": "Ethan", "last_name": "Nguyen"},
# {"first_name": "Ava", "last_name": "Johnson"},
# {"first_name": "Mason", "last_name": "Williams"},
# {"first_name": "Isabella", "last_name": "Garcia"},
# {"first_name": "William", "last_name": "Lee"},
# {"first_name": "Mia", "last_name": "Anderson"},
# {"first_name": "James", "last_name": "Taylor"},
# {"first_name": "Charlotte", "last_name": "Brown"},
# {"first_name": "Benjamin", "last_name": "Moore"},
# {"first_name": "Amelia", "last_name": "Davis"},
# {"first_name": "Lucas", "last_name": "Wilson"},
# {"first_name": "Harper", "last_name": "Martinez"},
# {"first_name": "Alexander", "last_name": "White"},
# {"first_name": "Evelyn", "last_name": "Scott"},
# {"first_name": "Daniel", "last_name": "Jackson"},
# {"first_name": "Abigail", "last_name": "Lewis"},
# {"first_name": "Michael", "last_name": "Robinson"},
# {"first_name": "Emily", "last_name": "Clark"},
# {"first_name": "David", "last_name": "Miller"},
# {"first_name": "Elizabeth", "last_name": "Hall"},
# {"first_name": "Joseph", "last_name": "Young"},
# {"first_name": "Sofia", "last_name": "Adams"},
# {"first_name": "Christopher", "last_name": "Allen"},
# {"first_name": "Grace", "last_name": "Turner"},
# {"first_name": "Matthew", "last_name": "Harris"},
# {"first_name": "Chloe", "last_name": "Baker"},
# {"first_name": "Andrew", "last_name": "King"},
# {"first_name": "Zoe", "last_name": "Wright"},
# {"first_name": "Ryan", "last_name": "Lopez"},
# {"first_name": "Lily", "last_name": "Green"},
# {"first_name": "Joshua", "last_name": "Phillips"},
# {"first_name": "Layla", "last_name": "Campbell"},
# {"first_name": "Samuel", "last_name": "Evans"},
# {"first_name": "Aria", "last_name": "Mitchell"},
# {"first_name": "Nathan", "last_name": "Carter"},
# {"first_name": "Audrey", "last_name": "Ross"},
# {"first_name": "Tyler", "last_name": "Cooper"},
# {"first_name": "Scarlett", "last_name": "Reed"},
# {"first_name": "Dylan", "last_name": "Murphy"},
# {"first_name": "Hannah", "last_name": "Cook"},
# {"first_name": "Isaac", "last_name": "Bennett"},
# {"first_name": "Leah", "last_name": "Morgan"},
# {"first_name": "Owen", "last_name": "Foster"},
# {"first_name": "Zoe", "last_name": "Peterson"},
# {"first_name": "Caleb", "last_name": "Rivera"}
# ]

list_of_students_with_courses = [
    {"name": "Emma Thompson", "course": introduction_to_psychology},
    {"name": "Liam Chen", "course": calculus_i},
    {"name": "Sophia Rodriguez", "course": ancient_civilizations},
    {"name": "Noah Patel", "course": principles_of_economics},
    {"name": "Emma Thompson", "course": organic_chemistry},
    {"name": "Ethan Nguyen", "course": introduction_to_computer_science},
    {"name": "Ava Johnson", "course": english_literature_shakespeare},
    {"name": "Mason Williams", "course": environmental_science},
    {"name": "Isabella Garcia", "course": digital_marketing_fundamentals},
    {"name": "William Lee", "course": human_anatomy_and_physiology},
    {"name": "Mia Anderson", "course": introduction_to_psychology},
    {"name": "James Taylor", "course": calculus_i},
    {"name": "Charlotte Brown", "course": ancient_civilizations},
    {"name": "Benjamin Moore", "course": principles_of_economics},
    {"name": "Amelia Davis", "course": organic_chemistry},
    {"name": "Emma Thompson", "course": introduction_to_computer_science},
    {"name": "Harper Martinez", "course": english_literature_shakespeare},
    {"name": "Alexander White", "course": environmental_science},
    {"name": "Evelyn Scott", "course": digital_marketing_fundamentals},
    {"name": "Daniel Jackson", "course": human_anatomy_and_physiology},
    {"name": "Abigail Lewis", "course": introduction_to_psychology},
    {"name": "Michael Robinson", "course": calculus_i},
    {"name": "Emily Clark", "course": ancient_civilizations},
    {"name": "David Miller", "course": principles_of_economics},
    {"name": "Elizabeth Hall", "course": organic_chemistry},
    {"name": "Joseph Young", "course": introduction_to_computer_science},
    {"name": "Sofia Adams", "course": english_literature_shakespeare},
    {"name": "Christopher Allen", "course": environmental_science},
    {"name": "Grace Turner", "course": digital_marketing_fundamentals},
    {"name": "Matthew Harris", "course": human_anatomy_and_physiology},
    {"name": "Chloe Baker", "course": introduction_to_psychology},
    {"name": "Andrew King", "course": calculus_i},
    {"name": "Zoe Wright", "course": ancient_civilizations},
    {"name": "Ryan Lopez", "course": principles_of_economics},
    {"name": "Lily Green", "course": organic_chemistry},
    {"name": "Joshua Phillips", "course": introduction_to_computer_science},
    {"name": "Layla Campbell", "course": english_literature_shakespeare},
    {"name": "Samuel Evans", "course": environmental_science},
    {"name": "Aria Mitchell", "course": digital_marketing_fundamentals},
    {"name": "Nathan Carter", "course": human_anatomy_and_physiology},
    {"name": "Audrey Ross", "course": introduction_to_psychology},
    {"name": "Tyler Cooper", "course": calculus_i},
    {"name": "Scarlett Reed", "course": ancient_civilizations},
    {"name": "Dylan Murphy", "course": principles_of_economics},
    {"name": "Hannah Cook", "course": organic_chemistry},
    {"name": "Isaac Bennett", "course": introduction_to_computer_science},
    {"name": "Leah Morgan", "course": english_literature_shakespeare},
    {"name": "Owen Foster", "course": environmental_science},
    {"name": "Zoe Peterson", "course": digital_marketing_fundamentals},
    {"name": "Caleb Rivera", "course": human_anatomy_and_physiology}
]

session.add_all(list_of_courses)
session.commit()

# students_to_add = [StudentsTable(**student) for student in list_of_students_with_courses]
# session.add_all(students_to_add)
# session.commit()

# Напишіть програму, яка додає нового студента до бази даних та додає його до певного курсу.
# Переконайтеся, що ці зміни коректно відображаються у базі даних.
# student = StudentsTable(name=fake.name(), course=fake.random_element(list_of_courses))
# session.add(student)
# session.commit()

# db_student_exist = session.query(StudentsTable).filter_by(name=student.name).first()
# assert student == db_student_exist

# Напишіть запити до бази даних, які повертають інформацію про студентів, зареєстрованих на певний курс
# db_course = session.query(StudentsTable).join(CoursesTable).filter(CoursesTable.course_title == 'Organic Chemistry').all()
# for item in db_course:
#     print(f'{item.name} study at {item.course.course_title}')
# print(f'{db_course}')
# done!!!

# Напишіть запити до бази даних, які повертають інформацію про курси, на які зареєстрований певний студент.
# db_student = session.query(StudentsTable).join(CoursesTable).filter(StudentsTable.name == 'Emma Thompson').all()
# for item in db_student:
#     print(f'{item.name} study at {item.course.course_title}')
# done!!!


# Реалізуйте можливість оновлення даних про студентів або курси, а також видалення студентів з бази даних.
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
