import tkinter
from tkinter import messagebox

from controller.constants import *
from view.authorization_window.authorization_window_settings import *


class AuthorizationWindow:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.state(MW_STATE)
        self.main_window.title(MW_TITLE)

        self.login = tkinter.StringVar()
        self.password = tkinter.StringVar()

        self.registration_panel = None

        self.controller = None

        self.show_window_elements()

    def start(self):
        self.main_window.mainloop()

    def close(self):
        self.main_window.destroy()

    def show_window_elements(self):
        self.registration_panel = tkinter.Frame(
            self.main_window
        )
        self.registration_panel.place(relx=MW_ELEMENTS_RELX, rely=MW_ELEMENTS_RELY, anchor=tkinter.CENTER)

        self.show_app_name()
        self.show_entries()
        self.show_button()

    def show_app_name(self):
        app_name = tkinter.Label(
            self.registration_panel, text=AN_TEXT,
            font=(AN_FONT, AN_FONT_SIZE, AN_FONT_FORMAT),
        )
        app_name.pack(padx=AN_PAD_X, pady=AN_PAD_Y)

    def show_entries(self):
        entries_panel = tkinter.Frame(
            self.registration_panel
        )
        entries_panel.pack()

        login_label = tkinter.Label(
            entries_panel, text='Логін', font=(LA_FONT, LA_FONT_SIZE)
        )
        login_label.grid(column=FIRST_COLUMN, row=FIRST_ROW)

        login_entry = tkinter.Entry(
            entries_panel, font=(E_FONT, E_FONT_SIZE),
            textvariable=self.login
        )
        login_entry.grid(column=SECOND_COLUMN, row=FIRST_ROW)

        password_label = tkinter.Label(
            entries_panel, text='Пароль', font=(LA_FONT, LA_FONT_SIZE)
        )
        password_label.grid(column=FIRST_COLUMN, row=SECOND_ROW)

        password_entry = tkinter.Entry(
            entries_panel, font=(E_FONT, E_FONT_SIZE),
            textvariable=self.password, show=E_MASK
        )
        password_entry.grid(column=SECOND_COLUMN, row=SECOND_ROW)

    def show_button(self):
        button_panel = tkinter.Frame(
            self.registration_panel
        )
        button_panel.pack()

        button_reg = tkinter.Button(
            button_panel, text='Увійти', font=(B_FONT, B_FONT_SIZE),
            bg=B_COLOR, fg=B_FONT_COLOR, command=self.on_login_button_click
        )
        button_reg.pack(pady=B_PAD_Y)

    def set_controller(self, controller):
        self.controller = controller

    def get_login(self):
        return self.login.get()

    def get_password(self):
        return self.password.get()

    def show_message(self, code):
        messagebox.showinfo(
            title=MB_FAIL_TITLE, message=SHOW_MESSAGE_CODES[code]
        )

    def on_login_button_click(self):
        self.controller.login_user()
