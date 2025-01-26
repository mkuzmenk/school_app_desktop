import tkinter
from page import Page
from window_settings import (L_PANEL_COLOR, L_PANEL_WIDTH, L_PANEL_SIDE, L_PANEL_FILL,
                             RB_FONT, RB_FONT_COLOR, RB_FONT_SIZE, RB_FONT_FORMAT,
                             RB_WIDTH, B_COLOR, B_FONT, B_FONT_SIZE, B_FONT_COLOR, E_FONT, E_FONT_SIZE)


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

        tax_label = tkinter.Label(registration_panel, text='ІПН', font=(RB_FONT, RB_FONT_SIZE))
        tax_entry = tkinter.Entry(registration_panel, font=(E_FONT, E_FONT_SIZE))

        first_name_label = tkinter.Label(registration_panel, text="Ім'я", font=(RB_FONT, RB_FONT_SIZE))
        first_name_entry = tkinter.Entry(registration_panel, font=(E_FONT, E_FONT_SIZE))

        second_name_label = tkinter.Label(registration_panel, text='Прізвище', font=(RB_FONT, RB_FONT_SIZE))
        second_name_entry = tkinter.Entry(registration_panel, font=(E_FONT, E_FONT_SIZE))

        surname_label = tkinter.Label(registration_panel, text='По-батькові', font=(RB_FONT, RB_FONT_SIZE))
        surname_entry = tkinter.Entry(registration_panel, font=(E_FONT, E_FONT_SIZE))

        birthday_label = tkinter.Label(registration_panel, text='День народження', font=(RB_FONT, RB_FONT_SIZE))
        birthday_entry = tkinter.Entry(registration_panel, font=(E_FONT, E_FONT_SIZE))

        id_class_label = tkinter.Label(registration_panel, text="ID класу (не обов'язково)", font=(RB_FONT, RB_FONT_SIZE))
        id_class_entry = tkinter.Entry(registration_panel, font=(E_FONT, E_FONT_SIZE))

        email_label = tkinter.Label(registration_panel, text='Пошта', font=(RB_FONT, RB_FONT_SIZE))
        email_entry = tkinter.Entry(registration_panel, font=(E_FONT, E_FONT_SIZE))

        password_label = tkinter.Label(registration_panel, text='Пароль', font=(RB_FONT, RB_FONT_SIZE))
        password_entry = tkinter.Entry(registration_panel, font=(E_FONT, E_FONT_SIZE))

        password_repeat_label = tkinter.Label(registration_panel, text='Повторіть пароль', font=(RB_FONT, RB_FONT_SIZE))
        password_repeat_entry = tkinter.Entry(registration_panel, font=(E_FONT, E_FONT_SIZE))

        complete_button = tkinter.Button(text='Завершити реєстрацію', bg=B_COLOR, font=(B_FONT, B_FONT_SIZE),
                                         fg=B_FONT_COLOR)

        registration_panel.pack()

        tax_label.grid(column=1, row=1)
        tax_entry.grid(column=2, row=1)

        first_name_label.grid(column=1, row=2)
        first_name_entry.grid(column=2, row=2)

        second_name_label.grid(column=1, row=3)
        second_name_entry.grid(column=2, row=3)

        surname_label.grid(column=1, row=4)
        surname_entry.grid(column=2, row=4)

        birthday_label.grid(column=1, row=5)
        birthday_entry.grid(column=2, row=5)

        id_class_label.grid(column=1, row=6)
        id_class_entry.grid(column=2, row=6)

        email_label.grid(column=1, row=7)
        email_entry.grid(column=2, row=7)

        password_label.grid(column=1, row=8)
        password_entry.grid(column=2, row=8)

        password_repeat_label.grid(column=1, row=9)
        password_repeat_entry.grid(column=2, row=9)

        complete_button.pack()
