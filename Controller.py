from test_data import *


class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    # def add_teacher(self):
    #     data = self.view.active_window.get_teacher_data()
    #
    #     ipn = data[REGISTRATION_LABELS_TEACHER[0]]
    #     name = data[REGISTRATION_LABELS_TEACHER[1]]
    #     last_name = data[REGISTRATION_LABELS_TEACHER[2]]
    #     surname = data[REGISTRATION_LABELS_TEACHER[3]]
    #     birthdate = data[REGISTRATION_LABELS_TEACHER[4]]
    #     group_id = data[REGISTRATION_LABELS_TEACHER[5]]
    #     email = data[REGISTRATION_LABELS_TEACHER[6]]
    #     login = data[REGISTRATION_LABELS_TEACHER[7]]
    #     phone = data[REGISTRATION_LABELS_TEACHER[8]]
    #     sex = data[REGISTRATION_LABELS_TEACHER[9]]
    #     password = data[REGISTRATION_LABELS_TEACHER[10]]
    #
    #     result = self.model.add_user_teacher(ipn, login, name, last_name, surname, birthdate, email, password, phone,
    #                                          sex, group_id)
    #
    #     if result:
    #         self.view.active_window.show_message(4)
    #     else:
    #         self.view.active_window.show_message(1)

    def add_user_to_database(self):
        user_role = self.view.active_window.get_user_role()

        data = self.view.active_window.get_user_registration_data(user_role)

        user_labels = [REGISTRATION_LABELS_TEACHER, REGISTRATION_LABELS_STUDENT]

        registration_labels = user_labels[user_role]

        if data is not None:
            ipn = data[registration_labels[0]]
            name = data[registration_labels[1]]
            last_name = data[registration_labels[2]]
            surname = data[registration_labels[3]]
            birthdate = data[registration_labels[4]]
            group_id = data[registration_labels[5]]
            email = data[registration_labels[6]]
            login = data[registration_labels[7]]
            phone = data[registration_labels[8]]
            sex = data[registration_labels[9]]
            password = data[registration_labels[10]]

            result = self.model.add_user(ipn, login, name, last_name, surname, birthdate, email, password, phone,
                                         sex, user_role + 2, group_id)

            if result:
                self.view.active_window.show_message(user_role + 4)
            else:
                self.view.active_window.show_message(1)

    def get_users(self):
        data = self.view.active_window.get_user_data()

        result_data = self.model.get_user(data[SEARCH_LABELS[0]], data[SEARCH_LABELS[1]])

        if not result_data:
            self.view.active_window.show_message(2)
            return

        self.view.active_window.show_found_students(result_data)

    def show_schedule(self):
        num_class = self.view.active_window.get_class_number()
        self.view.active_window.enable_options()
        self.view.active_window.disable_option(num_class)

        week = self.model.get_schedule(num_class)

        self.view.active_window.show_main_panel(week)

    def show_students(self):
        num_class = self.view.active_window.get_class_number()
        self.view.active_window.enable_options()
        self.view.active_window.disable_option(num_class)

        student_list = self.model.get_students(num_class)
        teacher = self.model.get_class_teacher(num_class)

        self.view.active_window.show_main_panel(student_list, teacher)

    def get_teachers(self):
        teachers = self.model.get_teachers()
        return teachers

    def change_class_teacher(self, new_teacher_id):
        old_teacher_id = self.view.active_window.get_current_teacher_id()

        num_class = self.view.active_window.get_class_number()

        self.model.change_group_teacher(old_teacher_id, new_teacher_id, num_class)
        self.view.active_window.close_change_teacher_window()
        self.show_students()
