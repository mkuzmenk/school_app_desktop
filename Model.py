import sqlalchemy
from DB import start_db
from DB import Users
from datetime import datetime, UTC


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

        except sqlalchemy.exc.DatabaseError as db_err:
            print(db_err)

            self.conn.rollback()
            print('Некоректні дані')
            return None
