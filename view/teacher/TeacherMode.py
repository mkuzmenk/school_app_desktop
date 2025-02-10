import tkinter

from view.Window import Window
from view.teacher.teacher_window_settings import *
from view.teacher.pages.Schedule import Schedule


class TeacherMode(Window):
    def __init__(self):
        super().__init__()

    def add_toolbar_buttons(self):
        schedule_button = tkinter.Button(
            self.toolbar_panel, text="Розклад", bg=TB_COLOR, fg=TB_FONT_COLOR, height=B_HEIGHT,
            font=(TB_FONT, TB_FONT_SIZE, TB_FONT_FORMAT), relief=tkinter.FLAT,
            command=lambda: self.on_toolbar_button_click(Schedule)
        )
        schedule_button.pack(side=tkinter.LEFT, pady=TB_BUTTONS_PAD_Y)
