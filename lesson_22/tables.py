from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from lesson_22.alchemy_base import Base

association_table = Table(
    'association_table',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_title', String, ForeignKey('courses.course_title'), primary_key=True)
)


class CoursesTable(Base):
    __tablename__ = 'courses'

    course_title = Column(String, primary_key=True)

    students = relationship('StudentsTable', secondary=association_table, back_populates='courses')


class StudentsTable(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    courses = relationship('CoursesTable', secondary=association_table, back_populates='students')
