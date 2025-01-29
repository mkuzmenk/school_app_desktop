import tkinter
from window_settings import *
from schedule_admin_page import Schedule
from user_registration_admin_page import UserRegistration
from edit_group_admin_page import EditGroup


class Window:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.state('zoomed')

        self.active_window = None

        self.add_toolbar()

    def run(self):
        self.main_window.mainloop()

    def add_toolbar(self):
        up_menu = tkinter.Frame(self.main_window, bg=TB_COLOR, height=100)
        up_menu.pack(side="top", fill="x")

        schedule_button = tkinter.Button(up_menu, text="Розклад", bg=TB_COLOR, fg=TB_FONT_COLOR, height=2,
                                         font=(TB_FONT, TB_FONT_SIZE, TB_FONT_FORMAT), relief=TB_RELIEF,
                                         command=self.__on_schedule_click)

        edit_group_button = tkinter.Button(up_menu, text="Редагувати клас", bg=TB_COLOR, fg=TB_FONT_COLOR,
                                           height=2, font=(TB_FONT, TB_FONT_SIZE, TB_FONT_FORMAT), relief=TB_RELIEF,
                                           command=self.__on_edit_group_click)

        input_users_button = tkinter.Button(up_menu, text="Додати users", bg=TB_COLOR, fg=TB_FONT_COLOR, height=2,
                                            font=(TB_FONT, TB_FONT_SIZE, TB_FONT_FORMAT), relief=TB_RELIEF,
                                            command=self.__on_input_users_click)

        search_string = tkinter.Entry(up_menu, bg=E_COLOR, relief=TB_RELIEF, font=(E_FONT, E_FONT_SIZE))

        schedule_button.pack(side="left", pady=30)
        edit_group_button.pack(side="left", pady=30)
        input_users_button.pack(side="left", pady=30)

        search_string.pack(side="right", pady=30, padx=30)

    def __on_schedule_click(self):
        if not isinstance(self.active_window, Schedule):
            self.active_window = None
            self.active_window = Schedule(self.main_window)

            print('opening SchedulePage')

            print(self.main_window.winfo_children())
            print(self.active_window)

    def __on_input_users_click(self):
        if not isinstance(self.active_window, UserRegistration):
            self.active_window = None
            self.active_window = UserRegistration(self.main_window)

            print('opening UserRegistrationPage')

            print(self.main_window.winfo_children())
            print(self.active_window)

    def __on_edit_group_click(self):
        if not isinstance(self.active_window, EditGroup):
            self.active_window = None
            self.active_window = EditGroup(self.main_window)

            print('opening EditGroupPage')

            print(self.main_window.winfo_children())
            print(self.active_window)
