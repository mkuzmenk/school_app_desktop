import tkinter

from window_settings import *
from schedule_admin_page import Schedule
from add_user_page import AddUser
from edit_group_admin_page import EditGroup
from find_user_admin_page import FindUser


class Window:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.state(W_STATE)
        self.main_window.title(W_START_TITLE)

        self.controller = None

        # self.main_window.geometry(WINDOW_GEOMETRY)

        self.active_window = None

        self.add_toolbar()

    def run(self):
        self.main_window.mainloop()

    def set_controller(self, controller):
        self.controller = controller

    def add_toolbar(self):
        up_menu = tkinter.Frame(
            self.main_window, bg=TB_COLOR, height=100
        )
        up_menu.pack(side=tkinter.TOP, fill=tkinter.X)

        schedule_button = tkinter.Button(
            up_menu, text="Розклад", bg=TB_COLOR, fg=TB_FONT_COLOR, height=2,
            font=(TB_FONT, TB_FONT_SIZE, TB_FONT_FORMAT), relief=tkinter.FLAT,
            command=lambda: self.__on_toolbar_button_click(Schedule)
        )

        edit_group_button = tkinter.Button(
            up_menu, text="Редагувати клас", bg=TB_COLOR, fg=TB_FONT_COLOR,
            height=2, font=(TB_FONT, TB_FONT_SIZE, TB_FONT_FORMAT), relief=tkinter.FLAT,
            command=lambda: self.__on_toolbar_button_click(EditGroup)
        )

        input_users_button = tkinter.Button(
            up_menu, text="Додати користувачів", bg=TB_COLOR, fg=TB_FONT_COLOR, height=2,
            font=(TB_FONT, TB_FONT_SIZE, TB_FONT_FORMAT), relief=tkinter.FLAT,
            command=lambda: self.__on_toolbar_button_click(AddUser)
        )

        find_user = tkinter.Button(
            up_menu, text="Знайти користувача", bg=TB_COLOR, fg=TB_FONT_COLOR, height=2,
            font=(TB_FONT, TB_FONT_SIZE, TB_FONT_FORMAT), relief=tkinter.FLAT,
            command=lambda: self.__on_toolbar_button_click(FindUser)
        )

        schedule_button.pack(side=tkinter.LEFT, pady=TB_BUTTONS_PAD_Y)
        edit_group_button.pack(side=tkinter.LEFT, pady=TB_BUTTONS_PAD_Y)
        input_users_button.pack(side=tkinter.LEFT, pady=TB_BUTTONS_PAD_Y)

        find_user.pack(side=tkinter.RIGHT, pady=TB_BUTTONS_PAD_Y)

    def __on_toolbar_button_click(self, page_class):
        if not isinstance(self.active_window, page_class):
            if self.active_window:
                self.active_window.__del__()
                self.active_window = None

            self.active_window = page_class(self.main_window, self.controller)

            print(f'opening {page_class}')

            print(self.main_window.winfo_children())
            print(self.active_window)
