from test_data import REGISTRATION_LABELS


class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view.active_window

    def add_teacher(self):
        data = self.view.get_teacher_data()

        if data is not None:
            ipn = data[REGISTRATION_LABELS[0]]
            name = data[REGISTRATION_LABELS[1]]
            last_name = data[REGISTRATION_LABELS[2]]
            surname = data[REGISTRATION_LABELS[3]]
            birthdate = data[REGISTRATION_LABELS[4]]
            group_id = int(data[REGISTRATION_LABELS[5]])
            email = data[REGISTRATION_LABELS[6]]
            login = data[REGISTRATION_LABELS[7]]
            phone = data[REGISTRATION_LABELS[8]]
            sex = data[REGISTRATION_LABELS[9]]
            password = data[REGISTRATION_LABELS[10]]

            self.model.add_user_teacher(ipn, login, name, last_name, surname, birthdate, email, password, phone,
                                        sex, group_id)

            print('added')