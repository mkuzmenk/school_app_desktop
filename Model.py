from DB import start_db
from DB import Users
from datetime import datetime

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
        teacher = Users(password=password, user_login=user_login, user_first_name=name, user_last_name=last_name,
                        user_surname=surname, user_phone=phone, user_email=email, user_sex=sex, user_birthday=birthdate,
                        user_tax_number=ipn, user_created_at=datetime.utcnow(), last_login=datetime.utcnow(),
                        user_changed_at=datetime.utcnow(), is_active=1, is_staff=1, is_superuser=0,
                        user_group_id_ref=group_id, user_role=2)

        self.conn.add(teacher)
        self.conn.commit()
