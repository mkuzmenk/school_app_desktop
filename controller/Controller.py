import tkinter

from controller.constants import *
from view.authorization_window.AuthorizationWindow import AuthorizationWindow
from view.main_windows.admin.AdminMode import AdminMode
from view.main_windows.teacher.TeacherMode import TeacherMode
from view.main_windows.teacher.pages.Homework import Homework
from view.main_windows.teacher.pages.Journal import Journal


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def login_user(self):
        login = self.view.get_login()
        password = self.view.get_password()

        user = self.model.get_user(login)

        if user:
            if user.password != password:
                self.view.show_message(CODE_WRONG_PASSWORD)

            else:
                self.model.change_last_login(user)

                user_id = user.user_id

                if user.user_role == TEACHER_ROLE_ID:
                    self.open_teacher_window(user_id)

                else:
                    self.open_admin_window(user_id)



        else:
            self.view.show_message(CODE_LOGIN_NOT_FOUND)

    def open_authorization_window(self):
        self.view.close()

        self.view = AuthorizationWindow()
        self.view.set_controller(self)

    def open_teacher_window(self, teacher_id):
        self.view.close()

        self.view = TeacherMode(teacher_id)
        self.view.set_controller(self)

    def open_admin_window(self, admin_id):
        self.view.close()

        self.view = AdminMode(admin_id)
        self.view.set_controller(self)

    def add_user_to_database(self):
        user_role = self.view.active_page.get_user_role()

        data = self.view.active_page.get_user_registration_data()

        labels = REGISTRATION_LABELS[user_role]

        result = None

        if data:
            # data - словник.
            group_id = self.get_group_by_name(data[labels[LABEL_GROUP_POS]])
            if group_id:
                ipn = data[labels[LABEL_TAX_POS]]
                name = data[labels[LABEL_FIRST_NAME_POS]]
                last_name = data[labels[LABEL_LAST_NAME_POS]]
                surname = data[labels[LABEL_SURNAME_POS]]
                birthdate = data[labels[LABEL_BIRTHDATE]]
                email = data[labels[LABEL_EMAIL_POS]]
                login = data[labels[LABEL_LOGIN_POS]]
                phone = data[labels[LABEL_PHONE_NUMBER_POS]]
                sex = data[labels[LABEL_SEX_POS]]
                password = data[labels[LABEL_PASSWORD_POS]]

                result = self.model.add_user(ipn, login, name, last_name, surname, birthdate, email, password, phone,
                                             sex, user_role + 2, group_id)

            if result:
                # Якщо user_role = 0 - виводиться повідомлення з кодом 4, якщо user_role = 1 - код 5
                self.view.show_message(user_role + 4)
            else:
                self.view.show_message(CODE_INVALID_DATA)

    def show_users(self):
        data = self.view.active_page.get_user_data()
        result_data = tuple()

        if data:
            result_data = self.model.get_users(
                data[SEARCH_LABELS[SEARCH_FIRST_NAME_POS]],
                data[SEARCH_LABELS[SEARCH_LAST_NAME_POS]]
            )

        if not result_data:
            self.view.show_message(CODE_USERS_NOT_FOUND)
        else:
            self.view.active_page.show_found_students(result_data)

    def show_schedule(self):
        num_class = self.view.active_page.get_class_number()

        self.view.active_page.enable_options()
        self.view.active_page.disable_option(num_class)

        week = self.model.get_schedule(num_class)

        self.view.active_page.show_main_panel(week)

    def show_students(self):
        num_class = self.view.active_page.get_class_number()

        self.view.active_page.enable_options()
        self.view.active_page.disable_option(num_class)

        student_list = self.model.get_students_for_schedule(num_class)
        teacher = self.model.get_class_teacher(num_class)

        self.view.active_page.show_main_panel(student_list, teacher)

    def get_teachers(self):
        teachers = self.model.get_teachers()
        return teachers

    def change_class_teacher(self, new_teacher_id):

        num_class = self.view.active_page.get_class_number()

        self.model.change_group_teacher(new_teacher_id, num_class)
        self.view.active_page.close_change_teacher_window()
        self.show_students()

    def get_groups(self):
        groups = self.model.get_groups()
        return groups

    def get_group_by_name(self, group_name):
        group = self.model.get_group_by_name(group_name)
        return group

    def change_student(self, email, group):
        self.model.change_student(email, group)
        self.view.active_page.close_change_student_window()
        self.show_students()

    def show_teacher_disciplines(self):
        teacher_id = self.view.get_user_id()
        teacher_disciplines = self.model.get_teacher_disciplines(teacher_id)

        if not teacher_disciplines:
            self.view.show_message(CODE_NO_DISCIPLINES)
            return

        if self.view.active_page:
            self.view.active_page.__del__()
            self.view.active_page = None

        self.view.active_page = Homework(self.view, self, teacher_disciplines)

    def show_teacher_discipline_tasks(self):
        teacher_id = self.view.get_user_id()
        option = self.view.active_page.get_option()

        discipline_name = self.view.active_page.disciplines[option - 1]

        discipline_id = DISCIPLINES_ID[discipline_name]

        discipline_homeworks = self.model.get_teacher_discipline_homeworks(teacher_id, discipline_id)

        self.view.active_page.homeworks = discipline_homeworks

        self.view.active_page.show_tasks_panel()

    def add_task_to_database(self):
        data = self.view.active_page.get_add_task_entries_data()

        if data:
            # data - словник.
            group_id = self.get_group_by_name(data[LABEL_TASK_GROUP_ID_POS])

            if group_id:
                topic = data[LABEL_TASK_TOPIC_POS]
                description = data[LABEL_TASK_DESCRIPTION_POS]
                deadline = f'{data[TASK_DATE_POS]} {data[TASK_TIME_POS]}'
                teacher_id = self.view.active_page.get_user_id()
                discipline_id = self.view.active_page.get_discipline_id()

                result = self.model.add_homework(topic, description, deadline, group_id, teacher_id, discipline_id)

                if result:
                    self.view.show_message(CODE_TASK_ADDED)
                else:
                    self.view.show_message(CODE_INVALID_DATA)

    def show_students_homeworks_subpage(self):
        homework = self.view.active_page.get_current_homework()

        homework_responses = self.model.get_homework_responses(homework.home_work_id)

        marks = []
        students = []

        for homework_response in homework_responses:
            mark_value = '-'
            if homework_response.home_work_mark_id_ref:
                mark_value = homework_response.mark_hw_resp.mark_value
                if mark_value == 0:
                    mark_value = 'Н/О'

            student_fl_name = (f'{homework_response.user_hw_resp.user_first_name} '
                               f'{homework_response.user_hw_resp.user_last_name}')

            marks.append(mark_value)
            students.append(student_fl_name)

        self.view.active_page.show_students_homeworks_subpage(marks, students, homework_responses, homework)

    def show_student_homework_description(self):
        homework_response = self.view.active_page.get_current_homework_response()

        description = homework_response.home_work_response

        date_of_sending = homework_response.home_work_response_created_at

        self.view.active_page.task_description.config(state=NORMAL)

        self.view.active_page.task_description.delete(TEXT_START_POS, tkinter.END)
        self.view.active_page.task_description.insert(tkinter.END, description)

        self.view.active_page.task_description.config(state=DISABLED)

        self.view.active_page.deadline.config(text=f'Дата здачі: {date_of_sending}')

    def delete_homework(self):
        homework = self.view.active_page.get_current_homework()

        self.model.delete_homework(homework.home_work_id)

        self.view.active_page.back_to_disciplines()

    def change_student_mark(self, mark):
        mark_value = MARK_VALUES[mark]

        current_option = self.view.active_page.get_student_option()
        homework_response = self.view.active_page.responses[current_option - 1]

        if homework_response.home_work_mark_id_ref:
            self.model.change_mark_value(homework_response, mark_value)

        else:
            self.create_mark(homework_response, mark_value)

        self.view.active_page.close_set_mark_window()
        self.show_students_homeworks_subpage()

    def create_mark(self, homework_response, mark_value):
        option = self.view.active_page.get_option()

        discipline_name = self.view.active_page.disciplines[option - 1]

        discipline_id = DISCIPLINES_ID[discipline_name]
        homework_id = homework_response.home_work_id_ref
        student_id = homework_response.home_work_user_id_ref
        teacher_id = homework_response.home_work_response_teacher_id_ref

        new_mark_id = self.model.create_mark(
            mark_value=mark_value, hw_id=homework_id, discipline_id=discipline_id,
            student_id=student_id, teacher_id=teacher_id
        )

        if new_mark_id:
            homework_response.home_work_mark_id_ref = new_mark_id
            self.model.conn.commit()

    def show_teacher_group_journal(self):
        teacher_id = self.view.get_user_id()
        teacher_disciplines = self.model.get_teacher_disciplines(teacher_id)

        if not teacher_disciplines:
            self.view.show_message(CODE_NO_DISCIPLINES)
            return

        if self.view.active_page:
            self.view.active_page.__del__()
            self.view.active_page = None

        self.view.active_page = Journal(self.view, self, teacher_disciplines)

    def show_discipline_marks(self):
        option = self.view.active_page.get_option()

        self.view.active_page.enable_options()
        self.view.active_page.disable_option(option)

        self.view.active_page.hide_main_panel()

        current_discipline_option = self.view.active_page.get_option()

        marks = self.model.get_marks(current_discipline_option)

        self.view.active_page.group_marks = marks

        self.view.active_page.show_main_panel()
