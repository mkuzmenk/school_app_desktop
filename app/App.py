from controller.Controller import Controller
from model.Model import Model
from view.authorization_window.AuthorizationWindow import AuthorizationWindow
from view.main_windows.teacher.TeacherMode import TeacherMode


class App:
    def __init__(self):
        # self.view = AuthorizationWindow()

        self.view = TeacherMode(4)

        self.model = Model()

        self.controller = Controller(self.model, self.view)

        self.view.set_controller(self.controller)

        self.view.start()

    def start(self):
        self.view.start()
