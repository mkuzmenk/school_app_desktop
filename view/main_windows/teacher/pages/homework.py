import tkinter
from tkinter import ttk
from tkinter.ttk import Combobox

from datetime import datetime

from controller.constants import *
from view.main_windows.teacher.teacher_window_settings import *

from view.main_windows.page import Page

from tkcalendar import Calendar
from tktimepicker import AnalogPicker, AnalogThemes

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

        self.calendar_date = tkinter.StringVar()
        self.time_deadline = tkinter.StringVar()

        self.buttons_panel = None

        self.responses = None

        self.button_go_back = None

        self.button_mark = None

        self.window_mark = None

        self.entries = []

        self.window_choose_date = None
        self.button_choose_date = None

        self.window_choose_time = None
        self.button_choose_time = None

        self.calendar = None
        self.time = None

        self.create_task_panel = None

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

        self.controller.show_teacher_discipline_tasks()

    def show_actions_panel(self):
        actions_panel = tkinter.Frame(
            self.main_window, width=A_PANEL_WIDTH
        )
        actions_panel.pack(side=tkinter.LEFT, fill=tkinter.Y)

        button = tkinter.Button(
            actions_panel, text='Створити нове завдання', bg=B_COLOR, font=(B_FONT, B_FONT_SIZE),
            fg=B_FONT_COLOR,
            command=self.on_create_task_click
        )
        button.pack()

    def get_user_id(self):
        return self.user_id

    def on_create_task_click(self):
        self.show_create_task_subpage()

    def show_tasks_panel(self):
        tasks_panel = tkinter.Frame(
            self.main_window, bg=TI_COLOR
        )
        tasks_panel.pack(side=tkinter.LEFT, fill=tkinter.Y)

        self.task_dictionary.clear()

        for i in range(len(self.homeworks)):
            homework = self.homeworks[i]

            option = tkinter.Radiobutton(
                tasks_panel, text=f'{homework.home_work_topic} | {homework.group_homework.group_name} клас',
                value=i + 1, bg=TI_COLOR, fg=TI_FONT_COLOR,
                width=TI_WIDTH, variable=self.task,
                font=(TI_FONT, TI_FONT_SIZE, TI_FONT_FORMAT),
                command=self.on_task_radiobutton_click
            )
            option.pack()

            self.task_dictionary[i + 1] = option

    def get_discipline_id(self):
        option = self.get_option()

        discipline_name = self.disciplines[option - 1]
        discipline_id = DISCIPLINES_ID[discipline_name]

        return discipline_id

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

        self.show_homework_main_panel(homework)
        self.show_homework_right_panel(responses, marks, students)

    def show_homework_main_panel(self, homework):
        self.homework_panel = tkinter.Frame(
            self.main_window, bg=HD_COLOR
        )
        self.homework_panel.pack(side=tkinter.LEFT, fill=tkinter.Y)

        topic = tkinter.Label(
            self.homework_panel, text=homework.home_work_topic,
            bg=HD_COLOR, fg=HD_FONT_COLOR,
            width=HD_WIDTH,
            font=(HD_FONT, HD_FONT_SIZE, HD_FONT_FORMAT),
        )
        topic.pack()

        self.deadline = tkinter.Label(
            self.homework_panel, text=f'Здати до {homework.home_work_deadline}',
            bg=HD_COLOR, fg=HD_FONT_COLOR,
            width=HD_WIDTH,
            font=(HD_FONT, HD_FONT_SIZE, HD_FONT_FORMAT),
        )
        self.deadline.pack()

        self.show_task_description(homework)

        self.button_go_back = tkinter.Button(
            self.homework_panel, text='← Назад', bg=B_COLOR,
            font=(B_FONT, B_FONT_SIZE),
            fg=B_FONT_COLOR, command=self.back_to_disciplines
        )
        self.button_go_back.pack(side=tkinter.BOTTOM)

        self.buttons_panel = tkinter.Frame(
            self.homework_panel
        )
        self.buttons_panel.pack()

        delete_homework_button = tkinter.Button(
            self.buttons_panel, text='Видалити завдання', bg=B_COLOR, font=(B_FONT, B_FONT_SIZE),
            fg=B_FONT_COLOR, command=self.on_delete_homework_click
        )
        delete_homework_button.pack(side=tkinter.LEFT)

    def show_task_description(self, homework):
        task_description_panel = tkinter.Frame(
            self.homework_panel
        )
        task_description_panel.pack()

        self.task_description = tkinter.Text(
            task_description_panel,
            bg=HT_COLOR, width=HT_WIDTH, height=HT_HEIGHT,
            font=(HT_FONT, HT_FONT_SIZE, HT_FONT_FORMAT),
        )

        scrollbar = tkinter.Scrollbar(
            task_description_panel, command=self.task_description.yview
        )
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        self.task_description.insert(tkinter.END, homework.home_work_description)
        self.task_description.config(state=DISABLED, yscrollcommand=scrollbar.set)

        self.task_description.pack()

    def show_homework_right_panel(self, responses, marks, students):
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

    def get_current_homework(self):
        homework_option = self.get_task_option()
        homework = self.homeworks[homework_option - 1]

        return homework

    def get_current_homework_response(self):
        current_option = self.get_student_option()
        homework_response = self.responses[current_option - 1]

        return homework_response

    def on_delete_homework_click(self):
        self.controller.delete_homework()

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
        self.controller.show_teacher_discipline_tasks()

    def show_mark_button(self):
        if self.button_mark:
            self.button_mark.destroy()

        self.button_mark = tkinter.Button(
            self.buttons_panel, text='Оцінити', bg=B_COLOR,
            font=(B_FONT, B_FONT_SIZE),
            fg=B_FONT_COLOR, command=self.open_set_mark_window
        )
        self.button_mark.pack(side=tkinter.LEFT)

    def open_set_mark_window(self):
        self.window_mark = tkinter.Tk()
        self.window_mark.geometry(SMW_GEOMETRY)
        self.window_mark.title(SMW_TITLE)

        selected_mark = tkinter.IntVar()
        mark_list = list(MARK_VALUES.keys())

        window_mark_box = Combobox(
            self.window_mark, values=mark_list, state=MWCB_STATE,
            textvariable=selected_mark, width=MWCB_WIDTH,
            font=(MWCB_FONT, MWCB_FONT_SIZE)
        )
        window_mark_box.pack(pady=LA_PAD_Y)

        button_change = tkinter.Button(
            self.window_mark, text='Поставити оцінку',
            bg=B_COLOR, font=(B_FONT, B_FONT_SIZE), fg=B_FONT_COLOR,
            command=lambda: self.controller.change_student_mark(window_mark_box.get())
        )
        button_change.pack()

    def close_set_mark_window(self):
        self.window_mark.destroy()

    def show_create_task_subpage(self):
        self.hide_page()

        self.create_task_panel = tkinter.Frame(
            self.main_window
        )
        self.create_task_panel.pack()

        groups = self.controller.get_groups()

        selected_group = tkinter.StringVar(value=CTCB_GROUP_NOT_DEFINED)

        label = tkinter.Label(
            self.create_task_panel, text=ADD_TASK_LABELS[LABEL_TASK_GROUP_ID_POS],
            font=(LA_FONT, LA_FONT_SIZE)
        )
        label.grid(column=FIRST_COLUMN, row=LABEL_TASK_GROUP_ID_POS + 1, pady=LA_PAD_Y)

        data_field = ttk.Combobox(
            self.create_task_panel, values=groups, state=CTCB_STATE,
            textvariable=selected_group, width=CTCB_WIDTH,
            font=(CTCB_FONT, CTCB_FONT_SIZE)
        )
        data_field.grid(column=SECOND_COLUMN, row=LABEL_TASK_GROUP_ID_POS + 1, pady=E_PAD_Y)

        self.entries.append(data_field)

        self.show_add_task_entries()

        button_complete_panel = tkinter.Frame(
            self.main_window
        )
        button_complete_panel.pack()

        complete_button = tkinter.Button(
            button_complete_panel, text='Завершити додавання', bg=B_COLOR,
            font=(B_FONT, B_FONT_SIZE), fg=B_FONT_COLOR,
            command=self.controller.add_task_to_database
        )
        complete_button.pack(pady=B_PAD_Y)

        button_back_panel = tkinter.Frame(
            self.main_window
        )
        button_back_panel.pack()

        button_go_back = tkinter.Button(
            button_back_panel, text='← Назад', bg=B_COLOR,
            font=(B_FONT, B_FONT_SIZE),
            fg=B_FONT_COLOR, command=self.back_to_disciplines
        )
        button_go_back.pack(pady=B_PAD_Y)

    def show_add_task_entries(self):
        for i in range(LABEL_TASK_GROUP_ID_POS + 1, len(ADD_TASK_LABELS)):
            label = tkinter.Label(
                self.create_task_panel, text=ADD_TASK_LABELS[i], font=(LA_FONT, LA_FONT_SIZE)
            )
            label.grid(column=FIRST_COLUMN, row=i + 1, pady=LA_PAD_Y)

            if i == LABEL_TASK_DESCRIPTION_POS:
                data_field = tkinter.Text(
                    self.create_task_panel, font=(E_FONT, E_FONT_SIZE),
                    width=CTDE_WIDTH, height=CTDE_HEIGHT
                )
                data_field.grid(column=SECOND_COLUMN, row=i + 1, pady=E_PAD_Y)

            elif i == LABEL_TASK_DEADLINE_POS:
                self.button_choose_date = tkinter.Button(
                    self.create_task_panel, text='Дата: (не вибрано)', bg=B_COLOR,
                    font=(B_FONT, B_FONT_SIZE),
                    fg=B_FONT_COLOR, command=self.open_choose_date
                )
                self.button_choose_date.grid(column=SECOND_COLUMN, row=i + 1, pady=E_PAD_Y)

                self.button_choose_time = tkinter.Button(
                    self.create_task_panel, text='Час: (не вибрано)', bg=B_COLOR,
                    font=(B_FONT, B_FONT_SIZE),
                    fg=B_FONT_COLOR, command=self.open_choose_time
                )
                self.button_choose_time.grid(column=THIRD_COLUMN, row=i + 1, pady=E_PAD_Y)

                self.entries.extend((self.calendar_date, self.time_deadline))
                break

            else:
                data_field = tkinter.Entry(
                    self.create_task_panel, font=(E_FONT, E_FONT_SIZE)
                )
                data_field.grid(column=SECOND_COLUMN, row=i + 1, pady=E_PAD_Y)

            self.entries.append(data_field)

    def get_add_task_entries_data(self):
        data = []

        for entry in self.entries:
            if isinstance(entry, tkinter.Text):
                data.append(entry.get(TEXT_START_POS, tkinter.END))
            else:
                data.append(entry.get())

        for data_value in data:
            if not data_value:
                self.parent.show_message(CODE_EMPTY_FIELDS)
                data.clear()
                return data

        return data

    def open_choose_date(self):
        self.window_choose_date = tkinter.Tk()
        self.window_choose_date.geometry(SDW_GEOMETRY)
        self.window_choose_date.title(SDW_TITLE)

        self.calendar = Calendar(self.window_choose_date, date_pattern='yyyy-mm-dd', mindate=datetime.today())
        self.calendar.pack(expand=True, fill="both")

        self.calendar.bind("<<CalendarSelected>>", self.on_date_selected)

    def on_date_selected(self, event):
        date = self.calendar.get_date()
        self.button_choose_date.config(text=f'Дата: {date}')
        self.calendar_date.set(date)
        self.window_choose_date.destroy()

    def open_choose_time(self):
        self.window_choose_time = tkinter.Tk()
        self.window_choose_time.geometry(SDW_GEOMETRY)
        self.window_choose_time.title(SDW_TITLE)

        self.time = AnalogPicker(self.window_choose_time)
        self.time.pack(expand=True, fill="both")
        button_close = tkinter.Button(
            self.window_choose_time, text='Підтвердити', bg=B_COLOR,
            font=(B_FONT, B_FONT_SIZE),
            fg=B_FONT_COLOR, command=self.on_time_selected
        )
        theme = AnalogThemes(self.time)
        theme.setNavyBlue()
        button_close.pack(pady=E_PAD_Y)

    def on_time_selected(self):
        # format from tuple to string
        time = "{}:{} {}".format(*self.time.time())

        # format from AM/PM to 24 hours
        time = datetime.strptime(time, '%I:%M %p').strftime("%H:%M")

        self.time_deadline.set(time)
        print(self.time_deadline.get())
        self.button_choose_time.config(text=f'Час: {self.time_deadline.get()}')
        self.window_choose_time.destroy()
