import tkinter
from window_settings import WINDOW_GEOMETRY, TB_FONT, TB_FONT_COLOR, TB_COLOR
from schedule_admin_page import Schedule
from user_registration_admin_page import UserRegistration


class Window:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry(WINDOW_GEOMETRY)

        self.active_window = None

        self.__add_toolbar()

        self.main_window.mainloop()

    def __add_toolbar(self):
        self.up_meny = tkinter.Frame(self.main_window, bg=TB_COLOR, height=100)
        self.up_meny.pack(side="top", fill="x")

        self.schedule_button = tkinter.Button(self.up_meny, text="Розклад", bg=TB_COLOR, fg=TB_FONT_COLOR, height=2,
                                              font=(TB_FONT, 22, "bold"), relief="flat", command=self.__on_schedule_click)

        self.edit_group_button = tkinter.Button(self.up_meny, text="Редагувати клас", bg=TB_COLOR, fg=TB_FONT_COLOR,
                                                height=2,
                                                font=(TB_FONT, 22, "bold"), relief="flat")

        self.input_users_button = tkinter.Button(self.up_meny, text="Додати users", bg=TB_COLOR, fg=TB_FONT_COLOR, height=2,
                                                 font=(TB_FONT, 22, "bold"), relief="flat", command=self.__on_input_users_click)

        self.search_string = tkinter.Entry(self.up_meny, bg=TB_COLOR, relief="flat")

        self.schedule_button.pack(side="left", pady=30)
        self.edit_group_button.pack(side="left", pady=30)
        self.input_users_button.pack(side="left", pady=30)
        self.search_string.pack(side="right", pady=30, padx=30)

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
