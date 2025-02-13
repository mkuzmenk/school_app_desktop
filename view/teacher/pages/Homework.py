import tkinter
from tkinter.ttk import Combobox

from controller.constants import *
from view.teacher.teacher_window_settings import *

from view.Page import Page

from controller.constants import MARK_VALUES


class Homework(Page):
    def __init__(self, window, controller, disciplines_data):
        self.user_id = window.user_id

        self.window = window
        self.controller = controller

        self.disciplines = disciplines_data
        self.selected_discipline = None
        self.homeworks = None

        self.task_dictionary = {}
        self.task = tkinter.IntVar(value=OPTION_DEFAULT_VALUE)

        self.deadline = None
        self.homework_panel = None
        self.task_description = None

        self.responses = None

        self.student_dictionary = {}
        self.student = tkinter.IntVar(value=OPTION_DEFAULT_VALUE)

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
                font=(RB_FONT, RB_FONT_SIZE, RB_FONT_FORMAT),
                command=self.on_discipline_radiobutton_click
            )
            option.pack()

            self.option_dictionary[i + 1] = option

    def on_discipline_radiobutton_click(self):
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
            self.main_window, bg=TI_COLOR
        )
        tasks_panel.pack(side=tkinter.LEFT, fill=tkinter.Y)

        self.task_dictionary.clear()

        for i in range(len(self.homeworks)):
            homework = self.homeworks[i]

            option = tkinter.Radiobutton(
                tasks_panel, text=f'{homework.home_work_topic}',
                value=i + 1, bg=TI_COLOR, fg=TI_FONT_COLOR,
                width=TI_WIDTH, variable=self.task,
                font=(TI_FONT, TI_FONT_SIZE, TI_FONT_FORMAT),
                command=self.on_task_radiobutton_click
            )
            option.pack()

            self.task_dictionary[i + 1] = option

    def get_user_id(self):
        return self.user_id

    def on_task_radiobutton_click(self):
        self.enable_task_options()
        self.disable_task_option(self.get_task_option())

        self.controller.show_students_homeworks_subpage()

    def get_task_option(self):
        return self.task.get()

    def enable_task_options(self):
        for task_option in self.task_dictionary.values():
            if task_option[STATE] == DISABLED:
                task_option[STATE] = NORMAL

    def disable_task_option(self, num):
        self.task_dictionary[num].configure(state=DISABLED)

    def show_students_homeworks_subpage(self, marks, students, responses, homework):
        self.hide_page()

        self.responses = responses

        self.show_homework_left_panel(homework)
        self.show_homework_main_panel(responses, marks, students)

    def show_homework_left_panel(self, homework):
        self.homework_panel = tkinter.Frame(
            self.main_window, bg=TI_COLOR
        )
        self.homework_panel.pack(side=tkinter.LEFT, fill=tkinter.Y)

        topic = tkinter.Label(
            self.homework_panel, text=homework.home_work_topic,
            bg=TI_COLOR, fg=TI_FONT_COLOR,
            width=TI_WIDTH,
            font=(TI_FONT, TI_FONT_SIZE, TI_FONT_FORMAT),
        )
        topic.pack()

        self.deadline = tkinter.Label(
            self.homework_panel, text=f'Здати до {homework.home_work_deadline}',
            bg=TI_COLOR, fg=TI_FONT_COLOR,
            width=TI_WIDTH,
            font=(TI_FONT, TI_FONT_SIZE, TI_FONT_FORMAT),
        )
        self.deadline.pack()

        self.task_description = tkinter.Label(
            self.homework_panel, text=homework.home_work_description,
            bg=TD_COLOR, width=TD_WIDTH, height=TD_HEIGHT,
            font=(TD_FONT, TD_FONT_SIZE, TD_FONT_FORMAT),
        )
        self.task_description.pack(side=tkinter.LEFT)

        self.button_go_back = tkinter.Button(self.homework_panel, text='← Назад', bg=B_COLOR, font=(B_FONT, B_FONT_SIZE),
            fg=B_FONT_COLOR)

        self.button_go_back.configure(command=self.back_to_disciplines)


        self.button_go_back.pack(side=tkinter.BOTTOM)

    def show_homework_main_panel(self, responses, marks, students):
        main_panel = tkinter.Frame(
            self.main_window, bg=SH_COLOR
        )
        main_panel.pack(side=tkinter.LEFT, fill=tkinter.Y)

        for i in range(len(responses)):
            mark_value = marks[i]
            student = students[i]

            option = tkinter.Radiobutton(
                main_panel, text=f'{student} {mark_value} балів',
                value=i + 1, bg=SH_COLOR, fg=SH_FONT_COLOR,
                variable=self.student, width=SH_WIDTH,
                font=(SH_FONT, SH_FONT_SIZE, SH_FONT_FORMAT),
                command=self.on_student_homework_click
            )
            option.pack()

            self.student_dictionary[i + 1] = option

    def on_student_homework_click(self):
        self.enable_student_options()
        self.disable_student_option(self.get_student_option())
        self.show_mark_button()

        self.button_go_back.configure(command=self.controller.show_students_homeworks_subpage)

        self.controller.show_student_homework_description()

    def enable_student_options(self):
        for option in self.student_dictionary.values():
            if option[STATE] == DISABLED:
                option[STATE] = NORMAL

    def disable_student_option(self, num):
        self.student_dictionary[num].configure(state=DISABLED)

    def get_student_option(self):
        return self.student.get()

    def back_to_disciplines(self):
        self.hide_page()
        self.show_page()
        self.disable_option(self.get_option())
        self.show_actions_panel()
        self.controller.show_teacher_discipline_homeworks()


    def show_mark_button(self):
        self.button_mark = tkinter.Button(self.homework_panel, text='Оцінити', bg=B_COLOR,
                                             font=(B_FONT, B_FONT_SIZE),
                                             fg=B_FONT_COLOR, command=self.open_set_mark_window)


        self.button_mark.pack(side=tkinter.BOTTOM)


    def open_set_mark_window(self):
        self.window_mark = tkinter.Tk()
        self.window_mark.geometry('600x600')
        self.window_mark.title('Оцінити')


        selected_mark = tkinter.IntVar()
        mark_list = list(MARK_VALUES.keys())

        self.window_mark_box = Combobox(
            self.window_mark, values=mark_list, state=MWCB_STATE,
            textvariable=selected_mark, width=MWCB_WIDTH,
            font=(MWCB_FONT, MWCB_FONT_SIZE)
        )

        button_change = tkinter.Button(
            self.window_mark, text=f'Поставити оцінку',
            bg=B_COLOR, font=(B_FONT, B_FONT_SIZE), fg=B_FONT_COLOR,
            command=lambda: self.controller.change_student_mark(self.window_mark_box.get())
        )

        self.window_mark_box.pack(pady=LA_PAD_Y)
        button_change.pack()

    def close_set_mark_window(self):
        self.window_mark.destroy()