import tkinter

from view.main_windows.teacher.teacher_window_settings import *
from view.main_windows.Window import Window
from view.main_windows.teacher.pages.Schedule import Schedule


class TeacherMode(Window):
    def __init__(self, teacher_id):
        super().__init__()

        self.user_id = teacher_id

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
            command=self.on_homework_button_click
        )
        schedule_button.pack(side=tkinter.LEFT, pady=TB_BUTTONS_PAD_Y)

        logoff_button = tkinter.Button(
            self.toolbar_panel, text="Вийти", bg=TB_COLOR, fg=TB_FONT_COLOR, height=B_HEIGHT,
            font=(TB_FONT, TB_FONT_SIZE, TB_FONT_FORMAT), relief=tkinter.FLAT,
            command=self.on_logoff_button_click
        )
        logoff_button.pack(side=tkinter.RIGHT, pady=TB_BUTTONS_PAD_Y)

    def on_homework_button_click(self):
        self.controller.show_teacher_disciplines()
