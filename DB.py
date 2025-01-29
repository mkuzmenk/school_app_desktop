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
    content_type_id = Column(mysql.INTEGER, nullable=False)
    codename = Column(mysql.VARCHAR(100), nullable=False)

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
    group_id = Column(mysql.INTEGER, ForeignKey('auth_group.id'), nullable=False)
    permission_id = Column(mysql.INTEGER, ForeignKey('auth_permission.id'), nullable=False)

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
    group_teacher_id_id = Column(mysql.INTEGER, nullable=True)

    def __init__(self, group_id, group_name):
        self.group_id = group_id
        self.group_name = group_name

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

    def __init__(self, homework_id, discipline_id, homework_text):
        self.homework_id = homework_id
        self.discipline_id = discipline_id
        self.homework_text = homework_text

    def __str__(self):
        return f'{self.homework_id} - Discipline: {self.discipline_id}'

class MarkTypes(Base):
    __tablename__ = 'mark_types'

    mark_type_id = Column(mysql.INTEGER, primary_key=True, autoincrement=True)
    mark_name = Column(mysql.VARCHAR(255), nullable=False)

    def __init__(self, mark_type_id, mark_name):
        self.mark_type_id = mark_type_id
        self.mark_name = mark_name

    def __str__(self):
        return f'{self.mark_type_id} - {self.mark_name}'



# engine works with PyMySQL package

engine = create_engine(f"mysql+pymysql://{DB_SETTINGS['DB_USERNAME']}:{DB_SETTINGS['PASSWORD']}@"
                           f"{DB_SETTINGS['SERVER_ADDRESS']}:{DB_SETTINGS['PORT_NUMBER']}/{DB_SETTINGS['DB_NAME']}")

Session = sessionmaker(engine)
Base.metadata.create_all(bind=engine)



# function for test
def get_all_roles():
    conn = Session()

    roles = conn.query(User_Roles).all()
    for role in roles:
        print(role)

    conn.close()


def check_relationship_roles():
    conn = Session()

    user_roles = conn.query(User_Roles).all()
    for role1 in user_roles:
        print(role1.User_Role_Name)

        if role1.all_users:
            for user in role1.all_users:
                print(user.User_Login, user.User_First_Name)
        else:
            print('no users here')

        print()

    conn.close()


def test():
    get_all_roles()
    print('fk check')
    check_relationship_roles()


test()
