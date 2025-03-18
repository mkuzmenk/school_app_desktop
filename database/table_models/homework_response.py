from database.db import *


class HomeworkResponse(Base):
    __tablename__ = 'homework_responses'

    home_work_response_id = Column(mysql.INTEGER, primary_key=True, autoincrement=True)
    home_work_response = Column(mysql.LONGTEXT, nullable=False)
    home_work_response_created_at = Column(mysql.DATETIME(fsp=6), nullable=False)
    home_work_mark_id_ref = Column(mysql.INTEGER, ForeignKey('marks.mark_id'))
    home_work_user_id_ref = Column(mysql.INTEGER, ForeignKey('users.user_id'), nullable=False)
    home_work_id_ref = Column(mysql.INTEGER, ForeignKey('homeworks.home_work_id'), nullable=False)
    home_work_response_teacher_id_ref = Column(mysql.INTEGER, ForeignKey('users.user_id'), nullable=True)

    mark_hw_resp = relationship('Mark', back_populates='hw_resp_mark',
                                foreign_keys='HomeworkResponse.home_work_mark_id_ref')

    user_hw_resp = relationship('User', back_populates='hw_resp_user',
                                foreign_keys='HomeworkResponse.home_work_user_id_ref')

    homework_hw_resp = relationship('Homework', back_populates='hw_resp_homework',
                                    foreign_keys='HomeworkResponse.home_work_id_ref')

    teacher_hw_resp = relationship('User', back_populates='hw_resp_teacher',
                                   foreign_keys='HomeworkResponse.home_work_response_teacher_id_ref')

    def __init__(self, home_work_response_id, home_work_response, home_work_response_created_at,
                 home_work_mark_id_ref, home_work_user_id_ref, home_work_id_ref):
        self.home_work_response_id = home_work_response_id
        self.home_work_response = home_work_response
        self.home_work_response_created_at = home_work_response_created_at
        self.home_work_mark_id_ref = home_work_mark_id_ref
        self.home_work_user_id_ref = home_work_user_id_ref
        self.home_work_id_ref = home_work_id_ref

    def __str__(self):
        return f'{self.home_work_response_id} - User: {self.home_work_user_id_ref} - Homework: {self.home_work_id_ref}'

from .mark import Mark # noqa: E402
from .user import User # noqa: E402
from .homework import Homework # noqa: E402
