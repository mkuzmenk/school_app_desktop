from sqlalchemy import create_engine, Column
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


class Discipline_Type(Base):
    __tablename__ = 'Discipline_Type'

    Discipline_ID = Column(mysql.SMALLINT(6), primary_key=True)
    Discipline_Name = Column(mysql.VARCHAR(255))

    def __init__(self, id, name):
        self.Discipline_ID = id
        self.Discipline_Name = name

    def __str__(self):
        return f'{self.Discipline_ID} - {self.Discipline_Name}'


class Homeworks(Base):
    __tablename__ = 'Homeworks'

    Home_Work_ID = Column(mysql.INTEGER(11), primary_key=True)
    Home_Work_Name = Column(mysql.VARCHAR(255))
    Home_Work_User_REF = Column(mysql.INTEGER(11))
    Home_Work_Group_REF = Column(mysql.VARCHAR(255))
    Home_Work_TimeTable_REF = Column(mysql.INTEGER(11))
    Home_Work_Desc = Column(mysql.VARCHAR(255))
    Home_Work_Deadline = Column(mysql.DATE)

    def __init__(self, id, name, user_ref, group_ref, timetable_ref, desc, deadline):
        self.Home_Work_ID = id
        self.Home_Work_Name = name
        self.Home_Work_User_REF = user_ref
        self.Home_Work_Group_REF = group_ref
        self.Home_Work_TimeTable_REF = timetable_ref
        self.Home_Work_Desc = desc
        self.Home_Work_Deadline = deadline


    def __str__(self):
        return f'{self.Home_Work_ID} - {self.Home_Work_Name}'


class Marks(Base):
    __tablename__ = 'Marks'

    Marks_ID = Column(mysql.BIGINT(20), primary_key=True)
    Mark_Value = Column(mysql.TINYINT(4))
    Mark_User_REF = Column(mysql.VARCHAR(255))
    Mark_Student_REF = Column(mysql.INTEGER(11))
    Mark_Time_Table_REF = Column(mysql.INTEGER(11))
    Mark_Discipline_Type_REF = Column(mysql.INTEGER(11))
    Mark_Type = Column(mysql.CHAR(255))

    def __init__(self, id, value, user_ref, student_ref, time_table_ref, discipline_type_ref, mark_type):
        self.Marks_ID = id
        self.Mark_Value = value
        self.Mark_User_REF = user_ref
        self.Mark_Student_REF = student_ref
        self.Mark_Time_Table_REF = time_table_ref
        self.Mark_Discipline_Type_REF = discipline_type_ref
        self.Mark_Type = mark_type


    def __str__(self):
        return f'{self.Marks_ID} - {self.Mark_Value} - {self.Mark_User_REF}'


class Time_Table(Base):
    __tablename__ = 'Time_Table'

    Time_Table_ID = Column(mysql.INTEGER(11), primary_key=True)
    Time_Table_User_REF = Column(mysql.INTEGER(11))
    Time_Table_GroupName = Column(mysql.VARCHAR(255))
    Time_Table_Cabinet = Column(mysql.SMALLINT(6))
    Time_Table_Start_Time = Column(mysql.DATETIME)
    Time_Table_End_Time = Column(mysql.DATETIME)

    def __init__(self, id, user_ref, group_name, cabinet, start_time, end_time):
        self.Time_Table_ID = id
        self.Time_Table_User_REF = user_ref
        self.Time_Table_GroupName = group_name
        self.Time_Table_Cabinet = cabinet
        self.Time_Table_Start_Time = start_time
        self.Time_Table_End_Time = end_time


    def __str__(self):
        return f'{self.Time_Table_ID} - {self.Time_Table_GroupName}'


class User_Group(Base):
    __tablename__ = 'User_Group'

    ID = Column(mysql.INTEGER(11), primary_key=True)
    User_REF = Column(mysql.INTEGER(11))
    Group_Name = Column(mysql.VARCHAR(255))

    def __init__(self, id, user_ref, group_name):
        self.ID = id
        self.User_REF = user_ref
        self.Group_Name = group_name

    def __str__(self):
        return f'{self.ID} - {self.Group_Name}'


class User_Roles(Base):
    __tablename__ = 'User_Roles'

    User_Role_ID = Column(mysql.SMALLINT(6), primary_key=True)
    User_Role_Name = Column(mysql.VARCHAR(255), primary_key=True)

    def __init__(self, id, name):
        self.User_Role_ID = id
        self.User_Role_Name = name

    def __str__(self):
        return f'{self.User_Role_ID} - {self.User_Role_Name}'


class Users(Base):
    __tablename__ = 'Users'

    User_ID = Column(mysql.INTEGER(11), primary_key=True, autoincrement=True, unique=True)
    User_Login = Column(mysql.INTEGER(11), unique=True)
    User_Password = Column(mysql.VARCHAR(24))
    User_First_Name = Column(mysql.VARCHAR(255))
    User_Last_Name = Column(mysql.VARCHAR(255))
    User_Surname = Column(mysql.VARCHAR(255), nullable=True)
    User_Phone = Column(mysql.VARCHAR(255))
    User_EMail = Column(mysql.VARCHAR(255))
    User_Sex = Column(mysql.CHAR(1), nullable=True)
    User_Birthday = Column(mysql.DATE)
    User_Role = Column(mysql.SMALLINT(6))
    User_Taxnumber = Column(mysql.INTEGER(11), nullable=True)
    User_Desc = Column(mysql.VARCHAR(255), nullable=True)
    User_Creation_Date = Column(mysql.DATETIME)
    User_DLC = Column(mysql.DATETIME)

    def __init__(self, id, login, password, first_name, last_name, surname, phone, email, sex, birthday, role, taxnumber, desc, creation_date, dlc):
        self.User_ID = id
        self.User_Login = login
        self.User_Password = password
        self.User_First_Name = first_name
        self.User_Last_Name = last_name
        self.User_Surname = surname
        self.User_Phone = phone
        self.User_EMail = email
        self.User_Sex = sex
        self.User_Birthday = birthday
        self.User_Role = role
        self.User_Taxnumber = taxnumber
        self.User_Desc = desc
        self.User_Creation_Date = creation_date
        self.User_DLC = dlc

    def __str__(self):
        return f'{self.User_ID} - {self.User_First_Name} - {self.User_Last_Name} - {self.User_Login} - {self.User_Role}'


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


def test():
    get_all_roles()

test()