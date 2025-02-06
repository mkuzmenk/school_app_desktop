import tkinter
from page import Page
from window_settings import *
from test_data import *


class AddUser(Page):
    def __init__(self, window, controller):
        self.entries = {}

        self.user_role = None
        self.button = None

        super().__init__(window, controller)

    def __str__(self):
        return 'UserRegistration'

    def hide_main_panel(self):
        for widget in self.main_window.winfo_children()[2:]:
            widget.destroy()

        self.entries = {}

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

        user_labels = [REGISTRATION_LABELS_TEACHER, REGISTRATION_LABELS_STUDENT]

        current_user_role = self.get_user_role()

        if current_user_role != -1:
            self.enable_options()
            self.disable_option(self.get_user_role())

            current_labels = user_labels[current_user_role]

            for i in range(len(current_labels)):
                label = tkinter.Label(
                    registration_panel, text=current_labels[i], font=(L_FONT, L_FONT_SIZE)
                )
                entry = tkinter.Entry(
                    registration_panel, font=(E_FONT, E_FONT_SIZE)
                )

                self.entries[current_labels[i]] = entry

                label.grid(column=1, row=i+1, pady=L_PAD_Y)
                entry.grid(column=2, row=i+1, pady=E_PAD_Y)

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

    def get_user_registration_data(self, option):
        data = dict()

        for i in self.entries.keys():
            data[i] = self.entries[i].get()

        registration_labels = None

        if option == 0:
            registration_labels = REGISTRATION_LABELS_TEACHER

            for key in data.keys():
                if not data[key] and key != registration_labels[5]:
                    self.show_message(0)
                    return

        elif option == 1:
            registration_labels = REGISTRATION_LABELS_STUDENT

            for key in data.keys():
                if not data[key] and key != registration_labels[5] and key != registration_labels[0]:
                    self.show_message(0)
                    return

        if data[registration_labels[5]] and not data[registration_labels[5]].isdigit():
            self.show_message(1)
            return

        group_id = data[registration_labels[5]]

        if group_id:
            data[registration_labels[5]] = int(group_id)
        else:
            data[registration_labels[5]] = None

        password = data[registration_labels[10]]
        password_repeat = data[registration_labels[11]]

        if password != password_repeat:
            self.show_message(3)
            return

        return data
