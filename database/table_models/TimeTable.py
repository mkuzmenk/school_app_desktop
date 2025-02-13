from database.DB import *


class TimeTable(Base):
    __tablename__ = 'time_table'

    time_table_id = Column(mysql.INTEGER, autoincrement=True, primary_key=True)
    time_table_cabinet = Column(mysql.SMALLINT, nullable=False)
    time_table_start_time = Column(mysql.TIME(fsp=6), nullable=False)
    time_table_end_time = Column(mysql.TIME(fsp=6), nullable=False)
    time_table_day = Column(mysql.VARCHAR(10), nullable=False)
    time_table_discipline_ref = Column(mysql.INTEGER, ForeignKey('disciplines.discipline_id'), nullable=True)
    time_table_group_id_ref = Column(mysql.INTEGER, ForeignKey('groups.group_id'), nullable=True)
    time_table_teacher_id_ref = Column(mysql.INTEGER, ForeignKey('users.user_id'), nullable=True)

    discipline_time_table = relationship('Discipline', back_populates='time_table_discipline',
                                         foreign_keys='TimeTable.time_table_discipline_ref')

    group_time_table = relationship('Group', back_populates='time_table_group',
                                    foreign_keys='TimeTable.time_table_group_id_ref')

    teacher_time_table = relationship('User', back_populates='time_table_teacher',
                                      foreign_keys='TimeTable.time_table_teacher_id_ref')

    def __init__(self, time_table_id, time_table_cabinet, time_table_start_time, time_table_end_time, time_table_day,
                 time_table_discipline_ref, time_table_group_id_ref, time_table_teacher_id_ref):
        self.time_table_id = time_table_id
        self.time_table_cabinet = time_table_cabinet
        self.time_table_start_time = time_table_start_time
        self.time_table_end_time = time_table_end_time
        self.time_table_day = time_table_day
        self.time_table_discipline_ref = time_table_discipline_ref
        self.time_table_group_id_ref = time_table_group_id_ref
        self.time_table_teacher_id_ref = time_table_teacher_id_ref

    def __str__(self):
        return f'{self.time_table_start_time} - {self.time_table_id}'

from .Homework import Homework # noqa: E402
from .Discipline import Discipline # noqa: E402
from .Homework import Homework # noqa: E402
from .User import User # noqa: E402
