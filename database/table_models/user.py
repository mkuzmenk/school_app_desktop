from database.db import *


class User(Base):
    __tablename__ = 'users'

    password = Column(mysql.VARCHAR(128), nullable=False)
    last_login = Column(mysql.DATETIME(fsp=6), nullable=True)
    user_id = Column(mysql.INTEGER, autoincrement=True, primary_key=True)
    user_login = Column(mysql.VARCHAR(50), nullable=False, unique=True)
    user_first_name = Column(mysql.VARCHAR(255), nullable=False)
    user_last_name = Column(mysql.VARCHAR(255), nullable=False)
    user_surname = Column(mysql.VARCHAR(255), nullable=True)
    user_phone = Column(mysql.VARCHAR(20), nullable=False)
    user_email = Column(mysql.VARCHAR(254), nullable=False, unique=True)
    user_sex = Column(mysql.VARCHAR(1), nullable=False)
    user_birthday = Column(mysql.DATE, nullable=False)
    user_tax_number = Column(mysql.VARCHAR(25), nullable=True)
    user_description = Column(mysql.LONGTEXT, nullable=True)
    user_created_at = Column(mysql.DATETIME(fsp=6), nullable=False)
    user_changed_at = Column(mysql.DATETIME(fsp=6), nullable=False)
    is_active = Column(mysql.TINYINT(1), nullable=False)
    is_staff = Column(mysql.TINYINT(1), nullable=False)
    is_superuser = Column(mysql.TINYINT(1), nullable=False)
    user_group_id_ref = Column(mysql.INTEGER, ForeignKey('groups.group_id'), nullable=True)
    user_role = Column(mysql.INTEGER, ForeignKey('user_roles.user_role_id'), nullable=True)

    hw_resp_user = relationship('HomeworkResponse', back_populates='user_hw_resp',
                                foreign_keys='HomeworkResponse.home_work_user_id_ref')

    group_user = relationship('Group', back_populates='user_group',
                              foreign_keys='User.user_group_id_ref')

    homework_user = relationship('Homework', back_populates='user_homework',
                                 foreign_keys='Homework.home_work_teacher_ref_id')

    mark_user = relationship('Mark', back_populates='user_mark',
                             foreign_keys='Mark.mark_student_id')

    teacherdiscipline_user = relationship('TeacherDiscipline', back_populates='user_teacherdiscipline',
                                          foreign_keys='TeacherDiscipline.teacher_id')

    userrole_user = relationship('UserRole', back_populates='user_userrole',
                                 foreign_keys='User.user_role')

    time_table_teacher = relationship('TimeTable', back_populates='teacher_time_table',
                                      foreign_keys='TimeTable.time_table_teacher_id_ref')

    group_teacher = relationship('Group', back_populates='teacher_group',
                                 foreign_keys='Group.group_teacher_id_id')

    hw_resp_teacher = relationship('HomeworkResponse', back_populates='teacher_hw_resp',
                                   foreign_keys='HomeworkResponse.home_work_response_teacher_id_ref')

    def __init__(self, password, user_login, user_first_name, user_last_name,
                 user_phone, user_email, user_sex, user_birthday, user_created_at,
                 user_changed_at, is_active, is_staff, is_superuser, last_login=None,
                 user_surname=None, user_tax_number=None, user_description=None, user_group_id_ref=None, user_role=None):
        self.password = password
        self.last_login = last_login
        self.user_login = user_login
        self.user_first_name = user_first_name
        self.user_last_name = user_last_name
        self.user_surname = user_surname
        self.user_phone = user_phone
        self.user_email = user_email
        self.user_sex = user_sex
        self.user_birthday = user_birthday
        self.user_tax_number = user_tax_number
        self.user_description = user_description
        self.user_created_at = user_created_at
        self.user_changed_at = user_changed_at
        self.is_active = is_active
        self.is_staff = is_staff
        self.is_superuser = is_superuser
        self.user_group_id_ref = user_group_id_ref
        self.user_role = user_role

    def __str__(self):
        return f'{self.user_last_name} - {self.user_first_name} - {self.user_email}'

from .homework_response import HomeworkResponse # noqa: E402
from .group import Group # noqa: E402
from .homework import Homework # noqa: E402
from .mark import Mark # noqa: E402
from .teacher_discipline import TeacherDiscipline # noqa: E402
from .user_role import UserRole # noqa: E402
from .time_table import TimeTable # noqa: E402
