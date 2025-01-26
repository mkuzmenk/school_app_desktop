import tkinter
from page import Page


class EditGroup(Page):
    def __init__(self, window):
        super().__init__(window)

    def show_left_panel(self):
        self.show_groups_in_left_panel()

    def show_main_panel(self):
        pass
