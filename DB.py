from sqlalchemy import create_engine, Column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.dialects import mysql


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

# бумбулейла бумбулятор


# я тут пишу !!! !!  ! ! !! ! ! ! 
