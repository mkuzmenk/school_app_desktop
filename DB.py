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

    auth_group_permissions = relationship('AuthGroupPermissions', 'auth_group')

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

    auth_permissions_group = relationship('AuthGroupPermissions', back_populates='auth_permission')

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

    auth_group = relationship('AuthGroup', back_populates='auth_group_permissions')
    auth_permission = relationship('AuthPermission', back_populates='auth_permissions_group')

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

# TODO: foreign relationship

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

    group_id = Column(mysql.INTEGER, primary_key=True, autoincrement=True)
    group_name = Column(mysql.VARCHAR(255), nullable=False)
    group_teacher_id_id = Column(mysql.INTEGER, ForeignKey('users.user_id'), nullable=True)

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
    home_work_group_id_ref = Column(mysql.INTEGER, nullable=True)
    home_work_timetable_ref = Column(mysql.INTEGER, nullable=True)
    home_work_user_ref_id = Column(mysql.INTEGER, nullable=True)

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

    def __init__(self, mark_type_id, mark_type_name):
        self.mark_type_id = mark_type_id
        self.mark_type_name = mark_type_name

    def __str__(self):
        return f'{self.mark_type_id} - {self.mark_type_name}'


class Marks(Base):
    mark_id = Column(mysql.INTEGER, autoincrement=True, primary_key=True)
    mark_value = Column(mysql.INTEGER, nullable=False)
    mark_created_at = Column(mysql.DATE, nullable=False)
    homework_id_ref = Column(mysql.INTEGER, ForeignKey('homeworks.home_work_id'), nullable=False)
    mark_discipline_type_ref = Column(mysql.INTEGER, ForeignKey('disciplines.discipline_id'), nullable=False)
    mark_student_id = Column(mysql.INTEGER, nullable=False)
    mark_teacher_id = Column(mysql.INTEGER, nullable=False)
    mark_type = Column(mysql.INTEGER, nullable=False)

    def __init__(self, mark_id, mark_value, mark_created_at, homework_id_ref, mark_discipline_type_ref, mark_student_id,
                 mark_teacher_id, mark_type):
        self.mark_id = mark_id
        self.mark_value = mark_value
        self.mark_created_at = mark_created_at
        self.homework_id_ref =homework_id_ref
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

    def __init__(self, password, last_login, user_id, user_login, user_first_name, user_last_name, user_surname,
                 user_phone, user_email, user_sex, user_birthday, user_tax_number, user_description, user_created_at,
                 user_changed_at, is_active, is_staff, is_superuser, user_group_id_ref, user_role):
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
        return f'{self.user_last_name} - {self.user_first_name} - {self.user_tax_number}'


class UserRoles(Base):
    __tablename__ = 'user_roles'

    user_role_id = Column(mysql.INTEGER, autoincrement=True, primary_key=True)
    user_role_name = Column(mysql.VARCHAR(50), nullable=False, unique=True)

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
    time_table_discipline_ref_id = Column(mysql.INTEGER, ForeignKey('disciplines.discipline_id'), nullable=True)
    time_table_group_id_ref_id = Column(mysql.INTEGER, ForeignKey('groups.group_id'), nullable=True)

    def __init__(self, time_table_id, time_table_cabinet, time_table_start_time, time_table_end_time, time_table_day,
                 time_table_discipline_ref_id, time_table_group_id_ref_id):
        self.time_table_id = time_table_id
        self.time_table_cabinet = time_table_cabinet
        self.time_table_start_time = time_table_start_time
        self.time_table_end_time = time_table_end_time
        self.time_table_day = time_table_day
        self.time_table_discipline_ref_id = time_table_discipline_ref_id
        self.time_table_group_id_ref_id = time_table_group_id_ref_id

    def __str__(self):
        return f'{self.time_table_start_time} - {self.time_table_id}'


class TeacherDiscipline(Base):
    __tablename__ = 'timetable_teacherdiscipline'

    id = Column(mysql.INTEGER, autoincrement=True, primary_key=True)
    discipline_id = Column(mysql.INTEGER, nullable=False)
    teacher_id = Column(mysql.INTEGER, nullable=False)

    def __init__(self, id, discipline_id, teacher_id):
        self.id = id
        self.discipline_id = discipline_id
        self.teacher_id = teacher_id

    def __str__(self):
        return f'{self.teacher_id} - {self.id}'

# engine works with PyMySQL package

engine = create_engine(f"mysql+pymysql://{DB_SETTINGS['DB_USERNAME']}:{DB_SETTINGS['PASSWORD']}@"
                       f"{DB_SETTINGS['SERVER_ADDRESS']}:{DB_SETTINGS['PORT_NUMBER']}/{DB_SETTINGS['DB_NAME']}")

Session = sessionmaker(engine)
Base.metadata.create_all(bind=engine)



# function for test
# def get_all_roles():
#     conn = Session()
#
#     roles = conn.query(User_Roles).all()
#     for role in roles:
#         print(role)
#
#     conn.close()
#
#
# def check_relationship_roles():
#     conn = Session()
#
#     user_roles = conn.query(User_Roles).all()
#     for role1 in user_roles:
#         print(role1.User_Role_Name)
#
#         if role1.all_users:
#             for user in role1.all_users:
#                 print(user.User_Login, user.User_First_Name)
#         else:
#             print('no users here')
#
#         print()
#
#     conn.close()


# def test():
#     get_all_roles()
#     print('fk check')
#     check_relationship_roles()
#
#
# test()
