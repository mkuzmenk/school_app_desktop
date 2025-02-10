import tkinter

from view.Window import Window
from view.admin.pages.AddUser import AddUser
from view.admin.pages.EditGroup import EditGroup
from view.admin.pages.FindUser import FindUser
from view.admin.pages.Schedule import Schedule
from view.admin.admin_window_settings import *


class AdminMode(Window):
    def __init__(self):
        super().__init__()

    def add_toolbar_buttons(self):
        schedule_button = tkinter.Button(
            self.toolbar_panel, text="Розклад", bg=TB_COLOR, fg=TB_FONT_COLOR, height=B_HEIGHT,
            font=(TB_FONT, TB_FONT_SIZE, TB_FONT_FORMAT), relief=tkinter.FLAT,
            command=lambda: self.on_toolbar_button_click(Schedule)
        )
        schedule_button.pack(side=tkinter.LEFT, pady=TB_BUTTONS_PAD_Y)

        edit_group_button = tkinter.Button(
            self.toolbar_panel, text="Редагувати клас", bg=TB_COLOR, fg=TB_FONT_COLOR,
            height=B_HEIGHT, font=(TB_FONT, TB_FONT_SIZE, TB_FONT_FORMAT), relief=tkinter.FLAT,
            command=lambda: self.on_toolbar_button_click(EditGroup)
        )
        edit_group_button.pack(side=tkinter.LEFT, pady=TB_BUTTONS_PAD_Y)

        input_users_button = tkinter.Button(
            self.toolbar_panel, text="Додати користувачів", bg=TB_COLOR, fg=TB_FONT_COLOR, height=B_HEIGHT,
            font=(TB_FONT, TB_FONT_SIZE, TB_FONT_FORMAT), relief=tkinter.FLAT,
            command=lambda: self.on_toolbar_button_click(AddUser)
        )
        input_users_button.pack(side=tkinter.LEFT, pady=TB_BUTTONS_PAD_Y)

        find_user = tkinter.Button(
            self.toolbar_panel, text="Знайти користувача", bg=TB_COLOR, fg=TB_FONT_COLOR, height=B_HEIGHT,
            font=(TB_FONT, TB_FONT_SIZE, TB_FONT_FORMAT), relief=tkinter.FLAT,
            command=lambda: self.on_toolbar_button_click(FindUser)
        )
        find_user.pack(side=tkinter.RIGHT, pady=TB_BUTTONS_PAD_Y)
