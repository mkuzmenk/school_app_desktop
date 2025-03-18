from database.db import *


class Group(Base):
    __tablename__ = 'groups'

    group_id = Column(mysql.INTEGER, primary_key=True, autoincrement=True, nullable=False)
    group_name = Column(mysql.VARCHAR(255), nullable=False)
    group_teacher_id_id = Column(mysql.INTEGER, ForeignKey('users.user_id'), nullable=True)

    user_group = relationship('User', back_populates='group_user',
                              foreign_keys='User.user_group_id_ref')

    teacher_group = relationship('User', back_populates='group_teacher',
                                 foreign_keys='Group.group_teacher_id_id')

    homework_group = relationship('Homework', back_populates='group_homework',
                                  foreign_keys='Homework.home_work_group_id_ref')

    time_table_group = relationship('TimeTable', back_populates='group_time_table',
                                    foreign_keys='TimeTable.time_table_group_id_ref')

    def __init__(self, group_id, group_name, group_teacher_id_id):
        self.group_id = group_id
        self.group_name = group_name
        self.group_teacher_id_id = group_teacher_id_id

    def __str__(self):
        return f'{self.group_name}'

from .user import User # noqa: E402
from .homework import Homework # noqa: E402
from .time_table import TimeTable # noqa: E402
