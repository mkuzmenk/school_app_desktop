from database.DB import *


class Discipline(Base):
    __tablename__ = 'disciplines'

    discipline_id = Column(mysql.INTEGER, primary_key=True, autoincrement=True)
    discipline_name = Column(mysql.VARCHAR(255), nullable=False)

    mark_discipline = relationship('Mark', back_populates='discipline_mark',
                                   foreign_keys='Mark.mark_discipline_type_ref')

    time_table_discipline = relationship('TimeTable', back_populates='discipline_time_table',
                                         foreign_keys='TimeTable.time_table_discipline_ref')

    teacherdiscipline_discipline = relationship('TeacherDiscipline',
                                                back_populates='discipline_teacherdiscipline',
                                                foreign_keys='TeacherDiscipline.discipline_id')

    def __init__(self, discipline_id, discipline_name):
        self.discipline_id = discipline_id
        self.discipline_name = discipline_name

    def __str__(self):
        return f'{self.discipline_id} - {self.discipline_name}'

from .Mark import Mark # noqa: E402
from .TeacherDiscipline import TeacherDiscipline # noqa: E402
from .TimeTable import TimeTable # noqa: E402
