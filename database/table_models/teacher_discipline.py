from database.db import *


class TeacherDiscipline(Base):
    __tablename__ = 'teacher_discipline'

    id = Column(mysql.INTEGER, autoincrement=True, primary_key=True)
    discipline_id = Column(mysql.INTEGER, ForeignKey('disciplines.discipline_id'), nullable=False)
    teacher_id = Column(mysql.INTEGER, ForeignKey('users.user_id'), nullable=False)

    discipline_teacherdiscipline = relationship('Discipline', back_populates='teacherdiscipline_discipline',
                                                foreign_keys='TeacherDiscipline.discipline_id')

    user_teacherdiscipline = relationship('User', back_populates='teacherdiscipline_user',
                                          foreign_keys='TeacherDiscipline.teacher_id')

    def __init__(self, id, discipline_id, teacher_id):
        self.id = id
        self.discipline_id = discipline_id
        self.teacher_id = teacher_id

    def __str__(self):
        return f'{self.teacher_id} - {self.id}'

from .discipline import Discipline # noqa: E402
from .user import User # noqa: E402
