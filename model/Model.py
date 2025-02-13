import sqlalchemy

from database.table_models.Discipline import Discipline
from database.table_models.Homework import Homework
from database.table_models.HomeworkResponse import HomeworkResponse
from database.table_models.Mark import Mark
from database.table_models.TeacherDiscipline import TeacherDiscipline
from database.table_models.User import User
from database.table_models.TimeTable import TimeTable
from database.table_models.Group import Group

from database.start_db import start_db
from datetime import datetime, UTC
from controller.constants import *


class Model:
    def __init__(self):
        self.Session = start_db()

        assert self.Session is not None, DB_CONN_NOT_FOUND  # if no connection, program won't run

        self.conn = self.Session()

    def __del__(self):
        if self.Session:
            self.Session().close()

    def add_user(self, ipn, user_login, name, last_name, surname, birthdate, email, password, phone, sex, user_role,
                 group_id=None):

        try:
            is_staff = IS_STAFF_FALSE

            if user_role != STUDENT_ROLE_ID:
                is_staff = IS_STAFF_TRUE

            teacher = User(
                password=password, user_login=user_login, user_first_name=name, user_last_name=last_name,
                user_surname=surname, user_phone=phone, user_email=email, user_sex=sex,
                user_birthday=birthdate, user_tax_number=ipn, user_created_at=datetime.now(UTC),
                last_login=datetime.now(UTC), user_changed_at=datetime.now(UTC), is_active=IS_ACTIVE_TRUE,
                is_staff=is_staff, is_superuser=IS_SUPERUSER_FALSE, user_group_id_ref=group_id, user_role=user_role
            )

            self.conn.add(teacher)
            self.conn.commit()
            return True

        except sqlalchemy.exc.DatabaseError:
            self.conn.rollback()
            return False

    def get_users(self, first_name, last_name):
        query = self.conn.query(User).filter(
            User.user_first_name.like(f'%{first_name}%'),
            User.user_last_name.like(f'%{last_name}%'),
        ).all()

        return query

    def get_user_name_last_name(self, user_id):
        query_user = self.conn.query(User).filter(
            User.user_id == user_id,
        ).first()

        return query_user.user_last_name, query_user.user_first_name

    def get_schedule(self, num_class):
        week = dict()

        for day in WEEKDAYS_DB:
            query = self.conn.query(TimeTable).join(TimeTable.group_time_table).filter(
                TimeTable.time_table_day == day,
                Group.group_name == num_class
            ).order_by(TimeTable.time_table_start_time).all()

            if query is None:
                continue

            week[day] = []

            num_lesson = 1

            for lesson in query:
                name = None
                if lesson.teacher_time_table:
                    surname = ''

                    last_name = lesson.teacher_time_table.user_last_name

                    first_name = lesson.teacher_time_table.user_first_name

                    if lesson.teacher_time_table.user_surname:
                        surname = lesson.teacher_time_table.user_surname

                    name = (f'{last_name} {first_name} '
                            f'{surname}')

                if name is None:
                    name = '---'

                data = (num_lesson, lesson.discipline_time_table.discipline_name,
                        name,
                        lesson.time_table_start_time.strftime(DATETIME_FORMAT))

                week[day].append(data)
                num_lesson += 1

        return week

    def get_students_for_schedule(self, num_class):
        query = self.conn.query(User).join(User.group_user).filter(
            User.user_role == STUDENT_ROLE_ID,
            Group.group_name == num_class
        ).order_by(User.user_last_name).all()

        data = []

        for student in query:
            surname = ''

            last_name = student.user_last_name

            first_name = student.user_first_name

            if student.user_surname:
                surname = student.user_surname

            name = (f'{last_name} {first_name} '
                    f'{surname}')

            email = student.user_email

            data.append((name, student.user_birthday.strftime(BIRTHDATE_FORMAT), email))

        return data

    def get_class_teacher(self, group_name):
        query_group = self.conn.query(Group).filter(Group.group_name == group_name).first()

        teacher_name = NO_TEACHER_NAME
        teacher_id = TEACHER_ID_DEFAULT

        if query_group.teacher_group:

            surname = ''
            teacher = query_group.teacher_group
            teacher_id = teacher.user_id

            if teacher.user_surname:
                surname = teacher.user_surname

            teacher_name = f'{teacher.user_last_name} {teacher.user_first_name} {surname}'

        return teacher_name, teacher_id

    def get_teachers(self):
        query = self.conn.query(User).filter(User.user_role == 2).order_by(User.user_last_name).all()

        teacher_dict = dict()

        for teacher in query:
            f_n = ''
            l_n = ''
            surname = ''
            if teacher.user_first_name:
                f_n = teacher.user_first_name

            if teacher.user_last_name:
                l_n = teacher.user_last_name

            if teacher.user_surname:
                surname = teacher.user_surname

            teacher_name = f'{l_n} {f_n} {surname}'

            teacher_dict[teacher_name] = teacher.user_id

        return teacher_dict

    def get_group(self, group_id):
        group = self.conn.query(Group).filter(
            Group.group_id == group_id
        ).first()

        return group

    def get_groups(self):
        query = self.conn.query(Group).order_by(Group.group_name).all()

        group_list = []
        for group in query:
            group_list.append(group)

        return group_list

    def change_group_teacher(self, new_teacher_id, group_name):

        # old group is where teacher are changing, new group is where new teacher came from

        query_new_teacher = self.conn.query(User).filter(User.user_id == new_teacher_id).first()
        query_group = self.conn.query(Group).filter(Group.group_name == group_name).first()

        if query_new_teacher.group_user:
            query_new_teacher.group_user.group_teacher_id_id = None
            self.conn.commit()

        query_new_teacher.user_group_id_ref = query_group.group_id

        if query_group.teacher_group:
            query_group.teacher_group.user_group_id_ref = None

        query_group.group_teacher_id_id = query_new_teacher.user_id

        self.conn.commit()
        return True

    def change_student(self, email, group):
        student = self.conn.query(User).filter(
            User.user_email == email
        ).first()

        new_group = self.conn.query(Group).filter(
            Group.group_name == group
        ).first()

        student.user_group_id_ref = new_group.group_id

        self.conn.commit()

    def get_teacher_discipline_homeworks(self, teacher_id, discipline_id):
        query = self.conn.query(Homework).filter(
            Homework.home_work_teacher_ref_id == teacher_id,
            Homework.home_work_discipline_ref == discipline_id
        ).all()

        homeworks_list = []

        for homework in query:
            homeworks_list.append(homework)

        return homeworks_list

    def get_teacher_disciplines(self, teacher_id):
        query = self.conn.query(TeacherDiscipline).filter(
            TeacherDiscipline.teacher_id == teacher_id
        ).all()

        teacher_disciplines = []

        for teacher_discipline in query:
            teacher_disciplines.append(teacher_discipline.discipline_teacherdiscipline.discipline_name)

        return teacher_disciplines

    def get_homework_responses(self, homework_id):
        query_responses = self.conn.query(HomeworkResponse).filter(
            HomeworkResponse.home_work_id_ref == homework_id
        ).all()

        return query_responses

    def get_mark_value(self, mark_id):
        query_mark = self.conn.query(Mark).filter(
            Mark.mark_id == mark_id
        ).first()

        return query_mark.mark_value

    def change_mark_value(self, hw_resp, new_mark_value):
        hw_resp.mark_hw_resp.mark_value = new_mark_value

        self.conn.commit()

    def create_mark(self, mark_value, hw_id, discipline_id, student_id, teacher_id):
        mark_id = None
        try:
            today = datetime.today().strftime('%Y-%m-%d')

            mark = Mark(mark_value=mark_value, mark_created_at=today, homework_id_ref=hw_id,
                        mark_discipline_type_ref=discipline_id, mark_student_id=student_id, mark_teacher_id=teacher_id)

            self.conn.add(mark)
            self.conn.commit()

            mark_id = mark.mark_id


        except sqlalchemy.exc.DatabaseError:
            self.conn.rollback()
            print('ошибка в марк')

        finally:
            return mark_id