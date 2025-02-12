import tkinter

from controller.constants import *
from view.teacher.teacher_window_settings import *

from view.Page import Page


class Homework(Page):
    def __init__(self, window, controller, disciplines_data):
        self.user_id = window.user_id

        self.disciplines = disciplines_data
        self.selected_discipline = None
        self.homeworks = None

        self.task_dictionary = {}
        self.task = tkinter.IntVar(value=OPTION_DEFAULT_VALUE)

        super().__init__(window, controller)

    def show_left_panel(self):
        left_panel = tkinter.Frame(
            self.main_window, bg=LE_PANEL_COLOR, width=LE_PANEL_WIDTH
        )
        left_panel.pack(side=tkinter.LEFT, fill=tkinter.Y)

        for i in range(len(self.disciplines)):
            teacher_discipline = self.disciplines[i]

            option = tkinter.Radiobutton(
                left_panel, text=f'{teacher_discipline}',
                value=i + 1, bg=LE_PANEL_COLOR, fg=RB_FONT_COLOR,
                width=RB_WIDTH, variable=self.option,
                font=(RB_FONT, RB_FONT_SIZE, RB_FONT_FORMAT), command=self.on_homework_radiobutton_click
            )
            option.pack()

            self.option_dictionary[i + 1] = option

    def on_homework_radiobutton_click(self):
        self.hide_main_panel()

        self.enable_options()
        self.disable_option(self.get_option())

        self.show_actions_panel()

        self.controller.show_teacher_discipline_homeworks()

    def show_actions_panel(self):
        actions_panel = tkinter.Frame(
            self.main_window, width=A_PANEL_WIDTH
        )
        actions_panel.pack(side=tkinter.LEFT, fill=tkinter.Y)

        button = tkinter.Button(
            actions_panel, text='Створити нове завдання', bg=B_COLOR, font=(B_FONT, B_FONT_SIZE),
            fg=B_FONT_COLOR
        )
        button.pack()

    def show_tasks_panel(self):
        tasks_panel = tkinter.Frame(
            self.main_window, bg=TT_COLOR
        )
        tasks_panel.pack(side=tkinter.LEFT, fill=tkinter.Y)

        self.task_dictionary.clear()

        for i in range(len(self.homeworks)):
            homework = self.homeworks[i]

            option = tkinter.Radiobutton(
                tasks_panel, text=f'{homework.home_work_topic}',
                value=i + 1, bg=TT_COLOR, fg=TT_FONT_COLOR,
                width=TT_WIDTH, variable=self.task,
                font=(TT_FONT, TT_FONT_SIZE, TT_FONT_FORMAT),
                command=self.on_task_radiobutton_click
            )
            option.pack()

            self.task_dictionary[i + 1] = option

    def get_user_id(self):
        return self.user_id

    def on_task_radiobutton_click(self):
        self.enable_task_options()
        self.disable_task_option(self.get_task_option())

    def get_task_option(self):
        return self.task.get()

    def enable_task_options(self):
        for task_option in self.task_dictionary.values():
            if task_option[STATE] == DISABLED:
                task_option[STATE] = NORMAL

    def disable_task_option(self, num):
        self.task_dictionary[num].configure(state=DISABLED)
