from controller.Controller import Controller
from model.Model import Model
from view.admin.AdminMode import AdminMode
from view.teacher.TeacherMode import TeacherMode
from controller.constants import *


class App:
    def __init__(self):
        self.model = Model()

        self.role = None
        self.input_role_with_console()

        if self.role == ADMIN_ROLE_ID:
            self.view = AdminMode()

        elif self.role == TEACHER_ROLE_ID:
            self.view = TeacherMode()

        self.controller = Controller(self.model, self.view)
        self.view.set_controller(self.controller)

    def start(self):
        self.view.start()

    def input_role_with_console(self):
        print(f"Ролі:\n"
              f"{ADMIN_ROLE_ID} - Адмін\n"
              f"{TEACHER_ROLE_ID} - Вчитель\n")

        role_id = int(input("Введіть свою роль: "))

        self.role = role_id
