import tkinter

from view.main_windows.window import Window
from view.main_windows.admin.pages.add_user import AddUser
from view.main_windows.admin.pages.edit_group import EditGroup
from view.main_windows.admin.pages.find_user import FindUser
from view.main_windows.admin.pages.schedule import Schedule
from view.main_windows.admin.admin_window_settings import *


class AdminMode(Window):
    def __init__(self, admin_id):
        super().__init__()

        self.user_id = admin_id

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
        find_user.pack(side=tkinter.LEFT, pady=TB_BUTTONS_PAD_Y)

        logoff_button = tkinter.Button(
            self.toolbar_panel, text="Вийти", bg=TB_COLOR, fg=TB_FONT_COLOR, height=B_HEIGHT,
            font=(TB_FONT, TB_FONT_SIZE, TB_FONT_FORMAT), relief=tkinter.FLAT,
            command=self.on_logoff_button_click
        )
        logoff_button.pack(side=tkinter.RIGHT, pady=TB_BUTTONS_PAD_Y)
