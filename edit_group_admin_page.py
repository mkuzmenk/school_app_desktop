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
        main_frame.pack(side='top')

        button_frame = tkinter.Frame(
            main_frame
        )
        button_frame.pack(side='bottom')

        table = tkinter.ttk.Treeview(
            main_frame, show='headings', columns=('#1', '#2', '#3')
        )
        table.heading('#1', text='L. F. S. name')
        table.heading('#2', text='Birthday')
        table.heading('#3', text='Group')

        scrollbar = tkinter.ttk.Scrollbar(
            main_frame, orient=tkinter.VERTICAL, command=table.yview
        )
        table.configure(yscrollcommand=scrollbar.set)

        for student in STUDENT_LST:
            table.insert("", tkinter.END, values=student)

        table.pack(side='left')
        scrollbar.pack(side='right', fill='y')

        change_student_group_button = tkinter.Button(
            button_frame, text='Перевести учня', bg=B_COLOR,
            font=(B_FONT, B_FONT_SIZE), fg=B_FONT_COLOR
        )
        change_student_group_button.pack(side=tkinter.LEFT)

        change_student_teacher_button = tkinter.Button(
            button_frame, text='Змінити класного керівника', bg=B_COLOR,
            font=(B_FONT, B_FONT_SIZE), fg=B_FONT_COLOR
        )
        change_student_teacher_button.pack(side=tkinter.LEFT)
