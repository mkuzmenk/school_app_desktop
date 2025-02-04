from test_data import *


class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_teacher(self):
        data = self.view.active_window.get_teacher_data()

        for key in data.keys():
            if not data[key] and key != REGISTRATION_LABELS[5]:
                self.view.active_window.show_message(0)
                return

        if data[REGISTRATION_LABELS[5]] and not data[REGISTRATION_LABELS[5]].isdigit():
            self.view.active_window.show_message(1)
            return

        ipn = data[REGISTRATION_LABELS[0]]

        name = data[REGISTRATION_LABELS[1]]
        last_name = data[REGISTRATION_LABELS[2]]
        surname = data[REGISTRATION_LABELS[3]]

        birthdate = data[REGISTRATION_LABELS[4]]

        group_id = data[REGISTRATION_LABELS[5]]

        if group_id:
            group_id = int(group_id)
        else:
            group_id = None

        email = data[REGISTRATION_LABELS[6]]
        login = data[REGISTRATION_LABELS[7]]
        phone = data[REGISTRATION_LABELS[8]]

        sex = data[REGISTRATION_LABELS[9]]

        password = data[REGISTRATION_LABELS[10]]
        password_repeat = data[REGISTRATION_LABELS[11]]

        if password != password_repeat:
            self.view.active_window.show_message(3)

        result = self.model.add_user_teacher(ipn, login, name, last_name, surname, birthdate, email, password, phone,
                                             sex, group_id)

        if result:
            self.view.active_window.show_message(4)
        else:
            self.view.active_window.show_message(1)

    def get_users(self):
        data = self.view.active_window.get_user_data()

        if (not data[SEARCH_LABELS[0]]) and (not data[SEARCH_LABELS[1]]):
            self.view.active_window.show_message(0)
            return

        result_data = self.model.get_user(data[SEARCH_LABELS[0]], data[SEARCH_LABELS[1]])

        if not result_data:
            self.view.active_window.show_message(2)
            return

        self.view.active_window.show_found_students(result_data)
