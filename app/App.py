from controller.Controller import Controller
from model.Model import Model
from view.authorization_window.AuthorizationWindow import AuthorizationWindow


class App:
    def __init__(self):
        self.view = AuthorizationWindow()

        self.model = Model()

        self.controller = Controller(self.model, self.view)

        self.view.set_controller(self.controller)

        self.view.start()

    def start(self):
        self.view.start()
