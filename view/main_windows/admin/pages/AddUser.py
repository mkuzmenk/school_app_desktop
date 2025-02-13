from tkinter import ttk

from view.main_windows.Page import Page
from view.main_windows.Window import *
from controller.constants import *


class AddUser(Page):
    def __init__(self, window, controller):
        self.data_fields = {}

        self.user_role = None

        self.registration_panel = None
        self.button_panel = None
        self.label_panel = None

        super().__init__(window, controller)

    def __str__(self):
        return ADD_USER_STR

    def hide_main_panel(self):
        # Усі віджети після індексу 1 є віджетами головної панелі.
        for widget in self.main_window.winfo_children()[2:]:
            widget.destroy()

        self.data_fields = {}

    def show_left_panel(self):
        left_panel = tkinter.Frame(
            self.main_window, bg=LE_PANEL_COLOR, width=LE_PANEL_WIDTH
        )
        left_panel.pack(side=tkinter.LEFT, fill=tkinter.Y)

        self.user_role = tkinter.IntVar(value=ROLE_DEFAULT_OPTION)
        self.option_dictionary = dict()

        for i in range(len(REGISTRATION_OPTIONS)):
            option = tkinter.Radiobutton(left_panel, text=REGISTRATION_OPTIONS[i], value=i, bg=LE_PANEL_COLOR,
                                         fg=RB_FONT_COLOR,
                                         width=RB_WIDTH, variable=self.user_role,
                                         font=(RB_FONT, RB_FONT_SIZE, RB_FONT_FORMAT),
                                         command=self.show_main_panel)

            self.option_dictionary[i] = option

            option.pack()

    def show_main_panel(self):
        self.hide_main_panel()

        self.registration_panel = tkinter.Frame(
            self.main_window
        )
        self.button_panel = tkinter.Frame(
            self.main_window
        )
        self.label_panel = tkinter.Frame(
            self.main_window
        )

        self.registration_panel.pack()
        self.button_panel.pack()

        self.label_panel.pack(side=tkinter.BOTTOM)

        if self.get_user_role() != ROLE_DEFAULT_OPTION:
            self.add_labels_and_entries()

    def add_labels_and_entries(self):
        current_user_role = self.get_user_role()

        self.enable_options()
        self.disable_option(self.get_user_role())

        current_labels = REGISTRATION_LABELS[current_user_role]

        for i in range(len(current_labels)):
            label = tkinter.Label(
                self.registration_panel, text=current_labels[i], font=(LA_FONT, LA_FONT_SIZE)
            )
            label.grid(column=FIRST_COLUMN, row=i + 1, pady=LA_PAD_Y)

            if i == LABEL_GROUP_POS:
                groups = self.controller.get_groups()
                groups.insert(LIST_START_POS, RCB_GROUP_NOT_DEFINED)

                selected_group = tkinter.StringVar(value=RCB_GROUP_NOT_DEFINED)

                data_field = ttk.Combobox(
                    self.registration_panel, values=groups, state=RCB_STATE,
                    textvariable=selected_group, width=RCB_WIDTH,
                    font=(RCB_FONT, RCB_FONT_SIZE)
                )
                data_field.grid(column=SECOND_COLUMN, row=i + 1, pady=E_PAD_Y)

                self.data_fields[current_labels[i]] = selected_group

            else:
                data_field = tkinter.Entry(
                    self.registration_panel, font=(E_FONT, E_FONT_SIZE)
                )
                data_field.grid(column=SECOND_COLUMN, row=i + 1, pady=E_PAD_Y)

                self.data_fields[current_labels[i]] = data_field

        complete_button = tkinter.Button(
            self.button_panel, text='Завершити реєстрацію', bg=B_COLOR, font=(B_FONT, B_FONT_SIZE),
            fg=B_FONT_COLOR, command=self.controller.add_user_to_database
        )
        complete_button.pack()

        self.add_bottom_label()

    def add_bottom_label(self):
        bottom_label = tkinter.Label(
            self.label_panel, text="* - Необов'язково", font=(LA_FONT, LA_FONT_SIZE)
        )
        bottom_label.pack()

    def get_user_role(self):
        return self.user_role.get()

    def get_user_registration_data(self):
        option = self.get_user_role()

        data = dict()

        for data_field in self.data_fields.keys():
            data[data_field] = self.data_fields[data_field].get()

        labels = REGISTRATION_LABELS[option]

        for key in data.keys():
            if not data[key] and ('*' not in key):
                self.parent.show_message(CODE_EMPTY_FIELDS)
                data.clear()
                return data

        group_id = data[labels[LABEL_GROUP_POS]]

        if group_id and group_id != RCB_GROUP_NOT_DEFINED and not group_id.isdigit():
            self.parent.show_message(CODE_INVALID_DATA)
            data.clear()
            return data

        if group_id == RCB_GROUP_NOT_DEFINED:
            data[labels[LABEL_GROUP_POS]] = None
        else:
            data[labels[LABEL_GROUP_POS]] = int(group_id)

        password = data[labels[LABEL_PASSWORD_POS]]
        password_repeat = data[labels[LABEL_PASSWORD_REPEAT_POS]]

        if password != password_repeat:
            self.parent.show_message(CODE_PASSWORDS_DONT_MATCH)
            data.clear()
            return data

        return data
