import tkinter

from view.teacher.teacher_window_settings import *
from view.Window import Window
from view.teacher.pages.Homework import Homework
from view.teacher.pages.Schedule import Schedule


class TeacherMode(Window):
    def __init__(self, teacher_id):
        super().__init__()

        self.user_id = teacher_id
        self.disciplines = None

    def add_toolbar_buttons(self):
        schedule_button = tkinter.Button(
            self.toolbar_panel, text="Розклад", bg=TB_COLOR, fg=TB_FONT_COLOR, height=B_HEIGHT,
            font=(TB_FONT, TB_FONT_SIZE, TB_FONT_FORMAT), relief=tkinter.FLAT,
            command=lambda: self.on_toolbar_button_click(Schedule)
        )
        schedule_button.pack(side=tkinter.LEFT, pady=TB_BUTTONS_PAD_Y)

        schedule_button = tkinter.Button(
            self.toolbar_panel, text="Домашні завдання", bg=TB_COLOR, fg=TB_FONT_COLOR, height=B_HEIGHT,
            font=(TB_FONT, TB_FONT_SIZE, TB_FONT_FORMAT), relief=tkinter.FLAT,
            command=lambda: self.on_toolbar_button_click(Homework)
        )
        schedule_button.pack(side=tkinter.LEFT, pady=TB_BUTTONS_PAD_Y)

    def get_user_id(self):
        return self.user_id

    def set_disciplines(self):
        self.disciplines = self.controller.get_teacher_disciplines()
