import sqlalchemy
from DB import start_db
from DB import Users, TimeTable, Groups
from datetime import datetime, UTC
from test_data import WEEKDAYS_DB


class Model:
    def __init__(self):
        self.Session = start_db()
        assert self.Session is not None, 'DB connection is not found'      # if no connection, program won't run

        self.conn = self.Session()

    def __del__(self):
        if self.Session:
            self.Session().close()

    def add_user_teacher(self, ipn, user_login, name, last_name, surname, birthdate, email, password, phone, sex,
                         group_id=None):

        try:
            teacher = Users(password=password, user_login=user_login, user_first_name=name, user_last_name=last_name,
                            user_surname=surname, user_phone=phone, user_email=email, user_sex=sex, user_birthday=birthdate,
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


    def get_students(self, num_class):
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

            class_name = '**Не визначено**'

            if student.group_user:
                class_name = student.group_user.group_name

            data.append((name, student.user_birthday.strftime("%Y-%m-%d"), class_name))

        return data
