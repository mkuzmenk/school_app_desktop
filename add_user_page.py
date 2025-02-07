import tkinter
from tkinter import ttk

from page import Page
from window_settings import *
from number_and_text_constants import *


class AddUser(Page):
    def __init__(self, window, controller):
        self.data_fields = {}

        self.user_role = None
        self.button = None

        super().__init__(window, controller)

    def __str__(self):
        return 'UserRegistration'

    def hide_main_panel(self):
        for widget in self.main_window.winfo_children()[2:]:
            widget.destroy()

        self.data_fields = {}

    def show_left_panel(self):
        left_panel = tkinter.Frame(
            self.main_window, bg=L_PANEL_COLOR, width=L_PANEL_WIDTH
        )
        left_panel.pack(side=tkinter.LEFT, fill=tkinter.Y)

        self.user_role = tkinter.IntVar(value=-1)
        self.option_dictionary = dict()

        for i in range(len(REGISTRATION_OPTIONS)):
            option = tkinter.Radiobutton(left_panel, text=REGISTRATION_OPTIONS[i], value=i, bg=L_PANEL_COLOR,
                                         fg=RB_FONT_COLOR,
                                         width=RB_WIDTH, variable=self.user_role,
                                         font=(RB_FONT, RB_FONT_SIZE, RB_FONT_FORMAT),
                                         command=self.show_main_panel)

            self.option_dictionary[i] = option

            option.pack()

    def show_main_panel(self):
        self.hide_main_panel()

        registration_panel = tkinter.Frame(
            self.main_window
        )
        button_panel = tkinter.Frame(
            self.main_window
        )
        label_panel = tkinter.Frame(
            self.main_window
        )

        current_user_role = self.get_user_role()

        if current_user_role != -1:
            self.enable_options()
            self.disable_option(self.get_user_role())

            current_labels = REGISTRATION_LABELS[current_user_role]

            for i in range(len(current_labels)):
                label = tkinter.Label(
                    registration_panel, text=current_labels[i], font=(L_FONT, L_FONT_SIZE)
                )
                label.grid(column=1, row=i + 1, pady=L_PAD_Y)

                # 5 - позиція, де знаходиться рядок "Клас*".
                if i == 5:
                    groups = self.controller.get_groups()
                    groups.insert(0, RCB_GROUP_NOT_DEFINED)

                    selected_group = tkinter.StringVar(value=RCB_GROUP_NOT_DEFINED)

                    data_field = ttk.Combobox(
                        registration_panel, values=groups, state=RCB_STATE,
                        textvariable=selected_group, width=RCB_WIDTH,
                        font=(RCB_FONT, RCB_FONT_SIZE)
                    )
                    data_field.grid(column=2, row=i + 1, pady=E_PAD_Y)

                    self.data_fields[current_labels[i]] = selected_group

                else:
                    data_field = tkinter.Entry(
                        registration_panel, font=(E_FONT, E_FONT_SIZE)
                    )
                    data_field.grid(column=2, row=i + 1, pady=E_PAD_Y)

                    self.data_fields[current_labels[i]] = data_field

            complete_button = tkinter.Button(
                button_panel, text='Завершити реєстрацію', bg=B_COLOR, font=(B_FONT, B_FONT_SIZE),
                fg=B_FONT_COLOR, command=self.controller.add_user_to_database
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

    def get_user_role(self):
        return self.user_role.get()

    def get_user_registration_data(self):
        option = self.get_user_role()

        data = dict()

        for data_field in self.data_fields.keys():
            data[data_field] = self.data_fields[data_field].get()

        current_registration_labels = REGISTRATION_LABELS[option]

        for key in data.keys():
            if not data[key] and ('*' not in key):
                self.show_message(0)
                return

        group_id = data[current_registration_labels[5]]

        if group_id and group_id != RCB_GROUP_NOT_DEFINED and not group_id.isdigit():
            self.show_message(1)
            return

        if group_id == RCB_GROUP_NOT_DEFINED:
            data[current_registration_labels[5]] = None

        else:
            data[current_registration_labels[5]] = int(group_id)

        password = data[current_registration_labels[10]]
        password_repeat = data[current_registration_labels[11]]

        if password != password_repeat:
            self.show_message(3)
            return

        return data
