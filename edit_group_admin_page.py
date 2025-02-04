import tkinter.ttk
from page import Page
from window_settings import *
from test_data import *


class EditGroup(Page):
    def __init__(self, window, controller):
        super().__init__(window, controller)

    def __str__(self):
        return 'EditGroup'

    def show_left_panel(self):
        self.show_groups_in_left_panel()

    def show_main_panel(self):
        main_frame = tkinter.Frame(
            self.main_window
        )
        main_frame.pack(side=tkinter.TOP)

        button_frame = tkinter.Frame(
            main_frame
        )
        button_frame.pack(side=tkinter.BOTTOM)

        table = tkinter.ttk.Treeview(
            main_frame, show='headings', columns=('#1', '#2', '#3'), height=TEG_HEIGHT
        )
        table.heading('#1', text='ПІБ')
        table.heading('#2', text='Дата народження')
        table.heading('#3', text='Клас')

        scrollbar = tkinter.ttk.Scrollbar(
            main_frame, orient=tkinter.VERTICAL, command=table.yview
        )
        table.configure(yscrollcommand=scrollbar.set)

        for student in STUDENT_LST:
            table.insert("", tkinter.END, values=student)

        table.pack(side=tkinter.LEFT)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        change_student_group_button = tkinter.Button(
            button_frame, text='Перевести учня', bg=B_COLOR,
            font=(B_FONT, B_FONT_SIZE), fg=B_FONT_COLOR
        )
        change_student_group_button.pack(side=tkinter.LEFT, padx=B_PAD_X, pady=B_PAD_Y)

        change_student_teacher_button = tkinter.Button(
            button_frame, text='Змінити класного керівника', bg=B_COLOR,
            font=(B_FONT, B_FONT_SIZE), fg=B_FONT_COLOR
        )
        change_student_teacher_button.pack(side=tkinter.LEFT, padx=B_PAD_X, pady=B_PAD_Y)
