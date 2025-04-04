from tkinter import ttk

from view.main_windows.page import Page
from view.main_windows.window import *
from controller.constants import *


class FindUser(Page):
    def __init__(self, window, controller):
        self.entries = []

        self.table_with_users = None

        super().__init__(window, controller)

    def __str__(self):
        return FIND_USER_STR

    def show_main_panel(self):
        label_with_entry_panel = tkinter.Frame(
            self.main_window
        )
        label_with_entry_panel.pack(side=tkinter.TOP)

        for label_text in SEARCH_LABELS:
            column = tkinter.Frame(
                label_with_entry_panel
            )
            column.pack(side=tkinter.LEFT)

            label = tkinter.Label(
                column, text=label_text, font=(LA_FONT, LA_FONT_SIZE)
            )
            label.pack()

            entry = tkinter.Entry(
                column, font=(E_FONT, E_FONT_SIZE)
            )
            self.entries.append(entry)
            entry.pack(padx=E_PAD_X)

        button_panel = tkinter.Frame(
            self.main_window
        )
        button_panel.pack()

        button = tkinter.Button(
            button_panel, text='Знайти користувача', bg=B_COLOR, font=(B_FONT, B_FONT_SIZE),
            fg=B_FONT_COLOR, command=self.controller.show_users
        )
        button.pack(pady=B_PAD_Y)

        table_panel = tkinter.Frame(
            self.main_window
        )
        table_panel.pack()

        self.table_with_users = ttk.Treeview(
            table_panel, show='headings', columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7'),
            height=TFS_HEIGHT
        )
        self.table_with_users.pack(side=tkinter.LEFT)

        scrollbar = tkinter.ttk.Scrollbar(
            table_panel, orient=tkinter.VERTICAL, command=self.table_with_users.yview
        )
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        self.table_with_users.configure(yscrollcommand=scrollbar.set)

        self.table_with_users.heading('#1', text='ID')
        self.table_with_users.heading('#2', text="Ім'я")
        self.table_with_users.heading('#3', text='Прізвище')
        self.table_with_users.heading('#4', text='По-батькові')
        self.table_with_users.heading('#5', text='ID групи')
        self.table_with_users.heading('#6', text='Дата народження')
        self.table_with_users.heading('#7', text='Пошта')

    def get_user_data(self):
        data = {}

        for i in range(len(self.entries)):
            data[SEARCH_LABELS[i]] = self.entries[i].get()

        if (not data[SEARCH_LABELS[SEARCH_FIRST_NAME_POS]]) and (not data[SEARCH_LABELS[SEARCH_LAST_NAME_POS]]):
            self.parent.show_message(CODE_EMPTY_FIELDS)
            data.clear()
            return data

        return data

    def show_found_students(self, data):
        self.table_with_users.delete(*self.table_with_users.get_children())

        for user in data:
            values = (user.user_id, user.user_first_name, user.user_last_name, user.user_surname,
                      user.user_group_id_ref, user.user_birthday, user.user_email)

            self.table_with_users.insert("", tkinter.END, values=values)
