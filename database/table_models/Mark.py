from database.DB import *


class Mark(Base):
    __tablename__ = 'marks'

    mark_id = Column(mysql.INTEGER, autoincrement=True, primary_key=True)
    mark_value = Column(mysql.INTEGER, nullable=False)
    mark_created_at = Column(mysql.DATE, nullable=False)
    homework_id_ref = Column(mysql.INTEGER, ForeignKey('homeworks.home_work_id'), nullable=False)
    mark_discipline_type_ref = Column(mysql.INTEGER, ForeignKey('disciplines.discipline_id'), nullable=False)
    mark_student_id = Column(mysql.INTEGER, ForeignKey('users.user_id'), nullable=False)
    mark_teacher_id = Column(mysql.INTEGER, nullable=False)
    mark_type = Column(mysql.INTEGER, ForeignKey('mark_types.mark_type_id'), nullable=False)

    hw_resp_mark = relationship('HomeworkResponse', back_populates='mark_hw_resp',
                                foreign_keys='HomeworkResponse.home_work_mark_id_ref')

    homework_mark = relationship('Homework', back_populates='mark_homework',
                                 foreign_keys='Mark.homework_id_ref')

    discipline_mark = relationship('Discipline', back_populates='mark_discipline',
                                   foreign_keys='Mark.mark_discipline_type_ref')

    user_mark = relationship('User', back_populates='mark_user',
                             foreign_keys='Mark.mark_student_id')

    marktype_mark = relationship('MarkType', back_populates='mark_marktype',
                                 foreign_keys='Mark.mark_type')

    def __init__(self, mark_id, mark_value, mark_created_at, homework_id_ref, mark_discipline_type_ref, mark_student_id,
                 mark_teacher_id, mark_type):
        self.mark_id = mark_id
        self.mark_value = mark_value
        self.mark_created_at = mark_created_at
        self.homework_id_ref = homework_id_ref
        self.mark_discipline_type_ref = mark_discipline_type_ref
        self.mark_student_id = mark_student_id
        self.mark_teacher_id = mark_teacher_id
        self.mark_type = mark_type

    def __str__(self):
        return f'{self.mark_id} - value {self.mark_value} - student {self.mark_student_id}'

from .HomeworkResponse import HomeworkResponse # noqa: E402
from .Homework import Homework # noqa: E402
from .Discipline import Discipline # noqa: E402
from .User import User # noqa: E402
from .MarkType import MarkType # noqa: E402
