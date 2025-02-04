import tkinter
from tkinter import messagebox
from page import Page
from window_settings import *
from test_data import *


class UserRegistration(Page):
    def __init__(self, window, controller):
        self.entries = {}

        self.button = None

        super().__init__(window, controller)

    def __str__(self):
        return 'UserRegistration'

    def show_left_panel(self):
        left_panel = tkinter.Frame(
            self.main_window, bg=L_PANEL_COLOR, width=L_PANEL_WIDTH
        )
        number_option = tkinter.IntVar(value=1)

        teacher_option = tkinter.Radiobutton(
            left_panel, text="Вчитель", value=1, bg=L_PANEL_COLOR, fg=RB_FONT_COLOR,
            width=RB_WIDTH,
            font=(RB_FONT, RB_FONT_SIZE, RB_FONT_FORMAT),
            variable=number_option
        )

        student_option = tkinter.Radiobutton(
            left_panel, text="Учень", value=1, bg=L_PANEL_COLOR, fg=RB_FONT_COLOR,
            width=RB_WIDTH,
            font=(RB_FONT, RB_FONT_SIZE, RB_FONT_FORMAT),
            variable=number_option
        )

        left_panel.pack(side=tkinter.LEFT, fill=tkinter.Y)

        student_option.pack()
        teacher_option.pack()

    def show_main_panel(self):
        registration_panel = tkinter.Frame(
            self.main_window
        )
        button_panel = tkinter.Frame(
            self.main_window
        )
        label_panel = tkinter.Frame(
            self.main_window
        )

        for i in range(len(REGISTRATION_LABELS)):
            label = tkinter.Label(
                registration_panel, text=REGISTRATION_LABELS[i], font=(L_FONT, L_FONT_SIZE)
            )
            entry = tkinter.Entry(
                registration_panel, font=(E_FONT, E_FONT_SIZE)
            )

            self.entries[REGISTRATION_LABELS[i]] = entry

            label.grid(column=1, row=i+1, pady=L_PAD_Y)
            entry.grid(column=2, row=i+1, pady=E_PAD_Y)

        complete_button = tkinter.Button(
            button_panel, text='Завершити реєстрацію', bg=B_COLOR, font=(B_FONT, B_FONT_SIZE),
            fg=B_FONT_COLOR, command=self.controller.add_teacher
        )

        self.button = complete_button

        registration_panel.pack()
        button_panel.pack()

        complete_button.pack()

        label_panel.pack(side=tkinter.BOTTOM)

        bottom_label = tkinter.Label(
            label_panel, text="* - Необов'язково", font=(L_FONT, L_FONT_SIZE)
        )
        bottom_label.pack()

    def get_teacher_data(self):
        data = dict()

        for i in self.entries.keys():
            data[i] = self.entries[i].get()

        return data

