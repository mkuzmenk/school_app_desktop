from sqlalchemy import create_engine, Column, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker, relationship
from sqlalchemy.dialects import mysql
from dotenv import load_dotenv
import os

load_dotenv()

DB_SETTINGS = {'SERVER_ADDRESS': os.getenv('SERVER_ADDRESS'),
               'DB_NAME': os.getenv('DB_NAME'),
               'DB_USERNAME': os.getenv('DB_USERNAME'),
               'PASSWORD': os.getenv('PASSWORD'),
               'PORT_NUMBER': os.getenv('PORT_NUMBER')
               }


class Base(DeclarativeBase):
    pass


class AuthGroup(Base):
    __tablename__ = 'auth_group'

    id = Column(mysql.INTEGER, primary_key=True, autoincrement=True)
    name = Column(mysql.VARCHAR(150), unique=True, nullable=False)

    auth_group_permissions = relationship('AuthGroupPermissions', back_populates='auth_group',
                                          foreign_keys='AuthGroupPermissions.group_id')

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'{self.id} - {self.name}'


class AuthPermission(Base):
    __tablename__ = 'auth_permission'

    id = Column(mysql.INTEGER, primary_key=True, autoincrement=True)
    name = Column(mysql.VARCHAR(255), nullable=False)
    content_type_id = Column(mysql.INTEGER, nullable=False, unique=True)
    codename = Column(mysql.VARCHAR(100), nullable=False, unique=True)

    auth_permissions_group = relationship('AuthGroupPermissions', back_populates='auth_permission',
                                          foreign_keys='AuthGroupPermissions.permission_id')

    def __init__(self, id, name, content_type_id, codename):
        self.id = id
        self.name = name
        self.content_type_id = content_type_id
        self.codename = codename

    def __str__(self):
        return f'{self.id} - {self.name} - {self.codename}'


class Disciplines(Base):
    __tablename__ = 'disciplines'

    discipline_id = Column(mysql.INTEGER, primary_key=True, autoincrement=True)
    discipline_name = Column(mysql.VARCHAR(255), nullable=False)

    mark_discipline = relationship('Marks', back_populates='discipline_mark',
                                   foreign_keys='Marks.mark_discipline_type_ref')

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


class AuthGroupPermissions(Base):
    __tablename__ = 'auth_group_permissions'

    id = Column(mysql.BIGINT, primary_key=True, autoincrement=True)
    group_id = Column(mysql.INTEGER, ForeignKey('auth_group.id'), nullable=False, unique=True)
    permission_id = Column(mysql.INTEGER, ForeignKey('auth_permission.id'), nullable=False, unique=True)

    auth_group = relationship('AuthGroup', back_populates='auth_group_permissions',
                              foreign_keys='AuthGroupPermissions.group_id')

    auth_permission = relationship('AuthPermission', back_populates='auth_permissions_group',
                                   foreign_keys='AuthGroupPermissions.permission_id')

    def __init__(self, id, group_id, permission_id):
        self.id = id
        self.group_id = group_id
        self.permission_id = permission_id

    def __str__(self):
        return f'{self.id} - Group: {self.group_id} - Permission: {self.permission_id}'


class HomeworkResponses(Base):
    __tablename__ = 'homework_responses'

    home_work_response_id = Column(mysql.INTEGER, primary_key=True, autoincrement=True)
    home_work_response = Column(mysql.LONGTEXT, nullable=False)
    home_work_response_created_at = Column(mysql.DATETIME(fsp=6), nullable=False)
    home_work_mark_id_ref = Column(mysql.INTEGER, ForeignKey('marks.mark_id'))
    home_work_user_id_ref = Column(mysql.INTEGER, ForeignKey('users.user_id'), nullable=False)
    home_work_id_ref = Column(mysql.INTEGER, ForeignKey('homeworks.home_work_id'), nullable=False)

    mark_hw_resp = relationship('Marks', back_populates='hw_resp_mark',
                                foreign_keys='HomeworkResponses.home_work_mark_id_ref')

    user_hw_resp = relationship('Users', back_populates='hw_resp_user',
                                foreign_keys='HomeworkResponses.home_work_user_id_ref')

    homework_hw_resp = relationship('Homeworks', back_populates='hw_resp_homework',
                                    foreign_keys='HomeworkResponses.home_work_id_ref')

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


class Groups(Base):
    __tablename__ = 'groups'

    group_id = Column(mysql.INTEGER, primary_key=True, autoincrement=True, nullable=False)
    group_name = Column(mysql.VARCHAR(255), nullable=False)
    group_teacher_id_id = Column(mysql.INTEGER, ForeignKey('users.user_id'), nullable=True)

    user_group = relationship('Users', back_populates='group_user', foreign_keys='Users.user_group_id_ref')

    teacher_group = relationship('Users', back_populates='group_teacher', foreign_keys='Groups.group_teacher_id_id')

    homework_group = relationship('Homeworks', back_populates='group_homework',
                                  foreign_keys='Homeworks.home_work_group_id_ref')

    time_table_group = relationship('TimeTable', back_populates='group_time_table',
                                    foreign_keys='TimeTable.time_table_group_id_ref')

    def __init__(self, group_id, group_name, group_teacher_id_id):
        self.group_id = group_id
        self.group_name = group_name
        self.group_teacher_id_id = group_teacher_id_id

    def __str__(self):
        return f'{self.group_id} - {self.group_name}'


class Homeworks(Base):
    __tablename__ = 'homeworks'

    home_work_id = Column(mysql.INTEGER, autoincrement=True, primary_key=True)
    home_work_name = Column(mysql.VARCHAR(255), nullable=False)
    home_work_topic = Column(mysql.VARCHAR(255), nullable=False)
    home_work_description = Column(mysql.LONGTEXT, nullable=False)
    home_work_deadline = Column(mysql.DATETIME(fsp=6), nullable=False)
    home_work_created_at = Column(mysql.DATETIME(fsp=6), nullable=False)
    home_work_group_id_ref = Column(mysql.INTEGER, ForeignKey('groups.group_id'), nullable=True)
    home_work_timetable_ref = Column(mysql.INTEGER, ForeignKey('time_table.time_table_id'), nullable=True)
    home_work_user_ref_id = Column(mysql.INTEGER, ForeignKey('users.user_id'), nullable=True)

    hw_resp_homework = relationship('HomeworkResponses', back_populates='homework_hw_resp',
                                    foreign_keys='HomeworkResponses.home_work_id_ref')

    mark_homework = relationship('Marks', back_populates='homework_mark',
                                 foreign_keys='Marks.homework_id_ref')

    group_homework = relationship('Groups', back_populates='homework_group',
                                  foreign_keys='Homeworks.home_work_group_id_ref')

    time_table_homework = relationship('TimeTable', back_populates='homework_time_table',
                                       foreign_keys='Homeworks.home_work_timetable_ref')

    user_homework = relationship('Users', back_populates='homework_user',
                                 foreign_keys='Homeworks.home_work_user_ref_id')

    def __init__(self, home_work_id, home_work_name, home_work_topic, home_work_description, home_work_deadline,
                 home_work_created_at, home_work_group_id_ref, home_work_timetable_ref, home_work_user_ref_id):
        self.home_work_id = home_work_id
        self.home_work_name = home_work_name
        self.home_work_topic = home_work_topic
        self.home_work_description = home_work_description
        self.home_work_deadline = home_work_deadline
        self.home_work_created_at = home_work_created_at
        self.home_work_group_id_ref = home_work_group_id_ref
        self.home_work_timetable_ref = home_work_timetable_ref
        self.home_work_user_ref_id = home_work_user_ref_id

    def __str__(self):
        return f'{self.home_work_id} - Group id ref: {self.home_work_group_id_ref}'


class MarkTypes(Base):
    __tablename__ = 'mark_types'

    mark_type_id = Column(mysql.INTEGER, primary_key=True, autoincrement=True)
    mark_type_name = Column(mysql.VARCHAR(255), nullable=False)

    mark_marktype = relationship('Marks', back_populates='marktype_mark',
                                 foreign_keys='Marks.mark_type')

    def __init__(self, mark_type_id, mark_type_name):
        self.mark_type_id = mark_type_id
        self.mark_type_name = mark_type_name

    def __str__(self):
        return f'{self.mark_type_id} - {self.mark_type_name}'


class Marks(Base):
    __tablename__ = 'marks'

    mark_id = Column(mysql.INTEGER, autoincrement=True, primary_key=True)
    mark_value = Column(mysql.INTEGER, nullable=False)
    mark_created_at = Column(mysql.DATE, nullable=False)
    homework_id_ref = Column(mysql.INTEGER, ForeignKey('homeworks.home_work_id'), nullable=False)
    mark_discipline_type_ref = Column(mysql.INTEGER, ForeignKey('disciplines.discipline_id'), nullable=False)
    mark_student_id = Column(mysql.INTEGER, ForeignKey('users.user_id'), nullable=False)
    mark_teacher_id = Column(mysql.INTEGER, nullable=False)
    mark_type = Column(mysql.INTEGER, ForeignKey('mark_types.mark_type_id'), nullable=False)

    hw_resp_mark = relationship('HomeworkResponses', back_populates='mark_hw_resp',
                                foreign_keys='HomeworkResponses.home_work_mark_id_ref')

    homework_mark = relationship('Homeworks', back_populates='mark_homework',
                                 foreign_keys='Marks.homework_id_ref')

    discipline_mark = relationship('Disciplines', back_populates='mark_discipline',
                                   foreign_keys='Marks.mark_discipline_type_ref')

    user_mark = relationship('Users', back_populates='mark_user', foreign_keys='Marks.mark_student_id')

    marktype_mark = relationship('MarkTypes', back_populates='mark_marktype',
                                 foreign_keys='Marks.mark_type')

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


class Users(Base):
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

    hw_resp_user = relationship('HomeworkResponses', back_populates='user_hw_resp',
                                foreign_keys='HomeworkResponses.home_work_user_id_ref')

    group_user = relationship('Groups', back_populates='user_group', foreign_keys='Users.user_group_id_ref')

    homework_user = relationship('Homeworks', back_populates='user_homework',
                                 foreign_keys='Homeworks.home_work_user_ref_id')

    mark_user = relationship('Marks', back_populates='user_mark', foreign_keys='Marks.mark_student_id')

    teacherdiscipline_user = relationship('TeacherDiscipline', back_populates='user_teacherdiscipline',
                                          foreign_keys='TeacherDiscipline.teacher_id')

    userrole_user = relationship('UserRoles', back_populates='user_userrole',
                                 foreign_keys='Users.user_role')

    time_table_teacher = relationship('TimeTable', back_populates='teacher_time_table',
                                      foreign_keys='TimeTable.time_table_teacher_id_ref')

    group_teacher = relationship('Groups', back_populates='teacher_group',
                                 foreign_keys='Groups.group_teacher_id_id')

    def __init__(self, password, user_login, user_first_name, user_last_name,
                 user_phone, user_email, user_sex, user_birthday, user_created_at,
                 user_changed_at, is_active, is_staff, is_superuser, last_login=None,
                 user_surname=None, user_tax_number=None, user_description=None, user_group_id_ref=None, user_role=None,
                 user_id=None):
        self.password = password
        self.last_login = last_login
        self.user_id = user_id
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


class UserRoles(Base):
    __tablename__ = 'user_roles'

    user_role_id = Column(mysql.INTEGER, autoincrement=True, primary_key=True)
    user_role_name = Column(mysql.VARCHAR(50), nullable=False, unique=True)

    user_userrole = relationship('Users', back_populates='userrole_user', foreign_keys='Users.user_role')

    def __init__(self, user_role_id, user_role_name):
        self.user_role_id = user_role_id
        self.user_role_name = user_role_name

    def __str__(self):
        return f'{self.user_role_name} - {self.user_role_id}'


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

    homework_time_table = relationship('Homeworks', back_populates='time_table_homework',
                                       foreign_keys='Homeworks.home_work_timetable_ref')

    discipline_time_table = relationship('Disciplines', back_populates='time_table_discipline',
                                         foreign_keys='TimeTable.time_table_discipline_ref')

    group_time_table = relationship('Groups', back_populates='time_table_group',
                                    foreign_keys='TimeTable.time_table_group_id_ref')

    teacher_time_table = relationship('Users', back_populates='time_table_teacher',
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


class TeacherDiscipline(Base):
    __tablename__ = 'teacher_discipline'

    id = Column(mysql.INTEGER, autoincrement=True, primary_key=True)
    discipline_id = Column(mysql.INTEGER, ForeignKey('disciplines.discipline_id'), nullable=False)
    teacher_id = Column(mysql.INTEGER, ForeignKey('users.user_id'), nullable=False)

    discipline_teacherdiscipline = relationship('Disciplines', back_populates='teacherdiscipline_discipline',
                                                foreign_keys='TeacherDiscipline.discipline_id')

    user_teacherdiscipline = relationship('Users', back_populates='teacherdiscipline_user',
                                          foreign_keys='TeacherDiscipline.teacher_id')

    def __init__(self, id, discipline_id, teacher_id):
        self.id = id
        self.discipline_id = discipline_id
        self.teacher_id = teacher_id

    def __str__(self):
        return f'{self.teacher_id} - {self.id}'


# engine works with PyMySQL package

def start_db():
    engine = create_engine(f"mysql+pymysql://{DB_SETTINGS['DB_USERNAME']}:{DB_SETTINGS['PASSWORD']}@"
                           f"{DB_SETTINGS['SERVER_ADDRESS']}:{DB_SETTINGS['PORT_NUMBER']}/{DB_SETTINGS['DB_NAME']}")

    Session = sessionmaker(engine)
    Base.metadata.create_all(bind=engine)
    return Session
