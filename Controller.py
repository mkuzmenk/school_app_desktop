from test_data import REGISTRATION_LABELS


class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_teacher(self):
        data = self.view.active_window.get_teacher_data()
        result_data = {}

        for key in data.keys():
            if not data[key] and key != "ID класу*":
                self.view.active_window.show_message_empty_teacher_fields()
                return

            result_data[key] = data[key]

        if result_data["ID класу*"] and not result_data["ID класу*"].isdigit():
            self.view.active_window.show_message_invalid_teacher_data()
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

        result = self.model.add_user_teacher(ipn, login, name, last_name, surname, birthdate, email, password, phone,
                                             sex, group_id)

        if result:
            self.view.active_window.show_message_success_teacher_added()
        else:
            self.view.active_window.show_message_invalid_teacher_data()
