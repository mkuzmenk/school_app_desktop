import sqlalchemy
from DB import start_db
from DB import Users, TimeTable, Groups
from datetime import datetime, UTC
from number_and_text_constants import WEEKDAYS_DB


class Model:
    def __init__(self):
        self.Session = start_db()

        assert self.Session is not None, 'DB connection is not found'  # if no connection, program won't run

        self.conn = self.Session()

        # pass

    def __del__(self):
        if self.Session:
            self.Session().close()

    def add_user_teacher(self, ipn, user_login, name, last_name, surname, birthdate, email, password, phone, sex,
                         group_id=None):

        try:
            teacher = Users(password=password, user_login=user_login, user_first_name=name, user_last_name=last_name,
                            user_surname=surname, user_phone=phone, user_email=email, user_sex=sex,
                            user_birthday=birthdate,
                            user_tax_number=ipn, user_created_at=datetime.now(UTC), last_login=datetime.now(UTC),
                            user_changed_at=datetime.now(UTC), is_active=1, is_staff=1, is_superuser=0,
                            user_group_id_ref=group_id, user_role=2)

            self.conn.add(teacher)
            self.conn.commit()
            return 1

        except sqlalchemy.exc.DatabaseError:
            self.conn.rollback()
            print('Некоректні дані')
            return None

    def add_user(self, ipn, user_login, name, last_name, surname, birthdate, email, password, phone, sex, user_role,
                 group_id=None):

        try:
            is_staff = 0

            if user_role != 3:
                is_staff = 1

            teacher = Users(password=password, user_login=user_login, user_first_name=name,
                            user_last_name=last_name,
                            user_surname=surname, user_phone=phone, user_email=email, user_sex=sex,
                            user_birthday=birthdate, user_tax_number=ipn, user_created_at=datetime.now(UTC),
                            last_login=datetime.now(UTC), user_changed_at=datetime.now(UTC), is_active=1,
                            is_staff=is_staff, is_superuser=0, user_group_id_ref=group_id, user_role=user_role)

            self.conn.add(teacher)
            self.conn.commit()
            return 1

        except sqlalchemy.exc.DatabaseError as ex:
            print(ex)

            self.conn.rollback()
            print('Некоректні дані')
            return None

    def get_user(self, first_name, last_name):
        query = self.conn.query(Users).filter(
            Users.user_first_name.like(f'%{first_name}%'),
            Users.user_last_name.like(f'%{last_name}%'),
        )

        return query.all()

    def get_schedule(self, num_class):
        week = dict()

        for day in WEEKDAYS_DB.values():
            query = self.conn.query(TimeTable).join(TimeTable.group_time_table).filter(
                TimeTable.time_table_day == day,
                Groups.group_name == num_class
            ).order_by(TimeTable.time_table_start_time).all()

            if query is None:
                continue

            week[day] = []

            num_lesson = 1

            for lesson in query:
                name = None
                if lesson.teacher_time_table:
                    last_name = ''
                    first_name = ''
                    surname = ''
                    if lesson.teacher_time_table.user_last_name:
                        last_name = lesson.teacher_time_table.user_last_name

                    if lesson.teacher_time_table.user_first_name:
                        first_name = lesson.teacher_time_table.user_first_name

                    if lesson.teacher_time_table.user_surname:
                        surname = lesson.teacher_time_table.user_surname

                    name = (f'{last_name} {first_name} '
                            f'{surname}')

                if name is None:
                    name = '---'

                data = (num_lesson, lesson.discipline_time_table.discipline_name,
                        name,
                        lesson.time_table_start_time.strftime("%H:%M"))

                week[day].append(data)
                num_lesson += 1

        return week

    def get_students_for_schedule(self, num_class):
        query = self.conn.query(Users).join(Users.group_user).filter(
            Users.user_role == 3,
            Groups.group_name == num_class
        ).order_by(Users.user_last_name).all()

        data = []

        for student in query:
            last_name = ''
            first_name = ''
            surname = ''
            if student.user_last_name:
                last_name = student.user_last_name

            if student.user_first_name:
                first_name = student.user_first_name

            if student.user_surname:
                surname = student.user_surname

            name = (f'{last_name} {first_name} '
                    f'{surname}')

            if name == '':
                name = '**Без імені**'

            email = '**Не вказано**'

            if student.user_email:
                email = student.user_email

            data.append((name, student.user_birthday.strftime("%Y-%m-%d"), email))

        return data

    def get_class_teacher(self, group_name):
        query_group = self.conn.query(Groups).filter(Groups.group_name == group_name).first()

        teacher_name = '---'
        teacher_id = -1

        if query_group.teacher_group:

            surname = ''
            teacher = query_group.teacher_group
            teacher_id = teacher.user_id

            if teacher.user_surname:
                surname = teacher.user_surname

            teacher_name = f'{teacher.user_last_name} {teacher.user_first_name} {surname}'

        return teacher_name, teacher_id

    def get_teachers(self):
        query = self.conn.query(Users).filter(Users.user_role == 2).order_by(Users.user_last_name).all()

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

    def get_groups(self):
        query = self.conn.query(Groups).order_by(Groups.group_name).all()

        group_list = []
        for group in query:
            group_list.append(group)

        return group_list

    def change_group_teacher(self, old_teacher_id, new_teacher_id, group_name):

        # old group is where teacher are changing, new group is where new teacher came from

        query_new_teacher = self.conn.query(Users).filter(Users.user_id == new_teacher_id).first()
        query_group = self.conn.query(Groups).filter(Groups.group_name == group_name).first()

        if old_teacher_id:
            query_old_teacher = self.conn.query(Users).filter(Users.user_id == old_teacher_id).first()

            query_old_teacher.user_group_id_ref = None

        query_new_teacher.user_group_id_ref = query_group.group_id

        query_group.group_teacher_id_id = query_new_teacher.user_id

        query_new_teacher.group_teacher.group_teacher_id_id = None

        self.conn.commit()
        return True
