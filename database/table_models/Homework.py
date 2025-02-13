from database.DB import *


class Homework(Base):
    __tablename__ = 'homeworks'

    home_work_id = Column(mysql.INTEGER, autoincrement=True, primary_key=True)
    home_work_topic = Column(mysql.VARCHAR(255), nullable=False)
    home_work_description = Column(mysql.LONGTEXT, nullable=False)
    home_work_deadline = Column(mysql.DATETIME(fsp=6), nullable=False)
    home_work_created_at = Column(mysql.DATETIME(fsp=6), nullable=False)
    home_work_group_id_ref = Column(mysql.INTEGER, ForeignKey('groups.group_id'), nullable=True)
    home_work_teacher_ref_id = Column(mysql.INTEGER, ForeignKey('users.user_id'), nullable=True)
    home_work_discipline_ref = Column(mysql.INTEGER, ForeignKey('disciplines.discipline_id'), nullable=True)

    hw_resp_homework = relationship('HomeworkResponse', back_populates='homework_hw_resp',
                                    foreign_keys='HomeworkResponse.home_work_id_ref')

    mark_homework = relationship('Mark', back_populates='homework_mark',
                                 foreign_keys='Mark.homework_id_ref')

    group_homework = relationship('Group', back_populates='homework_group',
                                  foreign_keys='Homework.home_work_group_id_ref')

    user_homework = relationship('User', back_populates='homework_user',
                                 foreign_keys='Homework.home_work_teacher_ref_id')

    def __init__(self, home_work_topic, home_work_description, home_work_deadline,
                 home_work_created_at, home_work_group_id_ref, home_work_teacher_ref_id,
                 home_work_discipline_ref):
        self.home_work_topic = home_work_topic
        self.home_work_description = home_work_description
        self.home_work_deadline = home_work_deadline
        self.home_work_created_at = home_work_created_at
        self.home_work_group_id_ref = home_work_group_id_ref
        self.home_work_teacher_ref_id = home_work_teacher_ref_id
        self.home_work_discipline_ref = home_work_discipline_ref

    def __str__(self):
        return f'{self.home_work_id} - Group id ref: {self.home_work_group_id_ref}'

from .HomeworkResponse import HomeworkResponse # noqa: E402
from .Mark import Mark # noqa: E402
from .Group import Group # noqa: E402
from .TimeTable import TimeTable # noqa: E402
from .User import User # noqa: E402
