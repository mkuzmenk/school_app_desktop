import tkinter
from tkinter import ttk

from view.main_windows.page import Page
from view.main_windows.teacher.teacher_window_settings import *


class Journal(Page):
    def __init__(self, window, controller, teacher_disciplines):
        self.disciplines = teacher_disciplines

        self.group_marks = None

        super().__init__(window, controller)

    def show_page(self):
        self.show_left_panel()

    def show_left_panel(self):
        left_panel = tkinter.Frame(
            self.main_window, bg=LE_PANEL_COLOR, width=LE_PANEL_WIDTH
        )
        left_panel.pack(side=tkinter.LEFT, fill=tkinter.Y)

        for i in range(len(self.disciplines)):
            discipline_name = self.disciplines[i]

            option = tkinter.Radiobutton(
                left_panel, text=f'{discipline_name}',
                value=i + 1, bg=LE_PANEL_COLOR, fg=RB_FONT_COLOR,
                width=RB_WIDTH, variable=self.option,
                font=(RB_FONT, RB_FONT_SIZE, RB_FONT_FORMAT),
                command=self.controller.show_discipline_marks
            )
            option.pack()

            self.option_dictionary[i + 1] = option

    def show_main_panel(self):
        main_panel = tkinter.Frame(
            self.main_window
        )
        main_panel.pack()

        discipline_marks_table = ttk.Treeview(
            main_panel, show='headings', columns=('#1', '#2', '#3', '#4'),
            height=TGM_HEIGHT
        )
        discipline_marks_table.heading('#1', text='ПІБ')
        discipline_marks_table.heading('#2', text='Клас')
        discipline_marks_table.heading('#3', text='Оцінка')
        discipline_marks_table.heading('#4', text='Дата виставлення завдання')

        discipline_marks_table.pack(side=tkinter.LEFT)

        scrollbar = tkinter.ttk.Scrollbar(
            main_panel, orient=tkinter.VERTICAL, command=discipline_marks_table.yview
        )
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        discipline_marks_table.configure(yscrollcommand=scrollbar.set)

        for group_mark in self.group_marks:
            discipline_marks_table.insert("", tkinter.END, values=group_mark)


