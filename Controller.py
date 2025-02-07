from number_and_text_constants import *


class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_user_to_database(self):
        user_role = self.view.active_window.get_user_role()

        data = self.view.active_window.get_user_registration_data()

        current_registration_labels = REGISTRATION_LABELS[user_role]

        if data is not None:
            ipn = data[current_registration_labels[0]]
            name = data[current_registration_labels[1]]
            last_name = data[current_registration_labels[2]]
            surname = data[current_registration_labels[3]]
            birthdate = data[current_registration_labels[4]]
            group_id = data[current_registration_labels[5]]
            email = data[current_registration_labels[6]]
            login = data[current_registration_labels[7]]
            phone = data[current_registration_labels[8]]
            sex = data[current_registration_labels[9]]
            password = data[current_registration_labels[10]]

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

        student_list = self.model.get_students_for_schedule(num_class)
        teacher = self.model.get_class_teacher(num_class)

        self.view.active_window.show_main_panel(student_list, teacher)

    def get_teachers(self):
        teachers = self.model.get_teachers()
        return teachers

    def change_class_teacher(self, new_teacher_id):

        num_class = self.view.active_window.get_class_number()

        self.model.change_group_teacher(new_teacher_id, num_class)
        self.view.active_window.close_change_teacher_window()
        self.show_students()

    def get_groups(self):
        groups = self.model.get_groups()
        return groups
