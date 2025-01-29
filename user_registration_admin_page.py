import tkinter
from page import Page
from window_settings import *
from test_data import *


class UserRegistration(Page):
    def __init__(self, window):
        super().__init__(window)

    def show_left_panel(self):
        left_panel = tkinter.Frame(self.main_window, bg=L_PANEL_COLOR, width=L_PANEL_WIDTH)

        number_option = tkinter.IntVar(value=1)

        teacher_option = tkinter.Radiobutton(left_panel, text="Вчитель", value=1, bg=L_PANEL_COLOR, fg=RB_FONT_COLOR,
                                             width=RB_WIDTH,
                                             font=(RB_FONT, RB_FONT_SIZE, RB_FONT_FORMAT),
                                             variable=number_option)

        student_option = tkinter.Radiobutton(left_panel, text="Учень", value=1, bg=L_PANEL_COLOR, fg=RB_FONT_COLOR,
                                             width=RB_WIDTH,
                                             font=(RB_FONT, RB_FONT_SIZE, RB_FONT_FORMAT),
                                             variable=number_option)

        left_panel.pack(side=L_PANEL_SIDE, fill=L_PANEL_FILL)

        student_option.pack()
        teacher_option.pack()

    def show_main_panel(self):
        registration_panel = tkinter.Frame(self.main_window)

        button_panel = tkinter.Frame(self.main_window)

        for i in range(len(REGISTRATION_LABELS)):
            label = tkinter.Label(registration_panel, text=REGISTRATION_LABELS[i], font=(RB_FONT, RB_FONT_SIZE))
            entry = tkinter.Entry(registration_panel, font=(E_FONT, E_FONT_SIZE))

            label.grid(column=1, row=i+1)
            entry.grid(column=2, row=i+1)

        complete_button = tkinter.Button(button_panel, text='Завершити реєстрацію', bg=B_COLOR, font=(B_FONT, B_FONT_SIZE),
                                         fg=B_FONT_COLOR)

        registration_panel.pack()

        button_panel.pack()
        complete_button.pack()
