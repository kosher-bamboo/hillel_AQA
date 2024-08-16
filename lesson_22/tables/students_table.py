from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from lesson_22.alchemy_base import Base


class StudentsTable(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    course_id = Column(Integer, ForeignKey('courses.course_id'))

    course = relationship('CoursesTable', back_populates='students')
