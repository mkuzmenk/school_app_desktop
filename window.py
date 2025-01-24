import tkinter
from window_constants import GEOMETRY, FONT, FONT_COLOR, TOOLBAR_COLOR
from schedule_admin_window import Schedule
from user_registration_admin_window import UserRegistration


class Window:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry(GEOMETRY)

        self.active_window = None

        self.__add_toolbar()

        self.main_window.mainloop()

    def __add_toolbar(self):
        self.up_meny = tkinter.Frame(self.main_window, bg=TOOLBAR_COLOR, height=100)
        self.up_meny.pack(side="top", fill="x")

        self.schedule_button = tkinter.Button(self.up_meny, text="Розклад", bg=TOOLBAR_COLOR, fg=FONT_COLOR, height=2,
                                              font=(FONT, 22, "bold"), relief="flat", command=self.__on_schedule_click)

        self.edit_group_button = tkinter.Button(self.up_meny, text="Редагувати клас", bg=TOOLBAR_COLOR, fg=FONT_COLOR,
                                                height=2,
                                                font=(FONT, 22, "bold"), relief="flat")

        self.input_users_button = tkinter.Button(self.up_meny, text="Додати users", bg=TOOLBAR_COLOR, fg=FONT_COLOR, height=2,
                                                 font=(FONT, 22, "bold"), relief="flat", command=self.__on_input_users_click)

        self.search_string = tkinter.Entry(self.up_meny, bg=TOOLBAR_COLOR, relief="flat")

        self.schedule_button.pack(side="left", pady=30)
        self.edit_group_button.pack(side="left", pady=30)
        self.input_users_button.pack(side="left", pady=30)
        self.search_string.pack(side="right", pady=30, padx=30)

    def __on_schedule_click(self):
        if not isinstance(self.active_window, Schedule):
            print('creating Schedule')
            self.active_window = Schedule(self.main_window)

    def __on_input_users_click(self):
        if not isinstance(self.active_window, UserRegistration):
            print('creating UserRegistration')
            self.active_window = UserRegistration(self.main_window)
