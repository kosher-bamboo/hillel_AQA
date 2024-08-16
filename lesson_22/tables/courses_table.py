from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from lesson_22.alchemy_base import Base


class CoursesTable(Base):
    __tablename__ = 'courses'

    course_id = Column(Integer, primary_key=True)
    course_title = Column(String)

    students = relationship('StudentsTable', back_populates='course')
