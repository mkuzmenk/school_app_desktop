import tkinter.ttk
from view.main_windows.page import Page
from view.main_windows.window import *
from controller.constants import *


class Schedule(Page):
    def __init__(self, window, controller):
        self.num_class = None
        self.schedule_frame = None
        super().__init__(window, controller)

    def __str__(self):
        return SCHEDULE_STR

    def show_left_panel(self):
        self.show_groups_in_left_panel()

    def show_main_panel(self, data=None):
        week = data

        if week is not None:
            self.schedule_frame = self.create_schedule_frame(self.schedule_frame)
            self.schedule_frame.pack()

            current_day = 0

            for i in range(TS_QUANTITY):

                column = tkinter.Frame(
                    self.schedule_frame
                )
                column.pack(side=tkinter.LEFT)

                for day in range(current_day, (len(week) // TS_QUANTITY + current_day)):

                    table_frame = tkinter.Frame(
                        column
                    )
                    table_frame.pack()

                    day_name = tkinter.Label(
                        table_frame, text=WEEKDAYS[current_day],
                        font=(R_PANEL_FONT, R_PANEL_FONT_SIZE)
                    )
                    day_name.pack()

                    table = tkinter.ttk.Treeview(
                        table_frame, show='headings', columns=('#1', '#2', '#3', '#4'), height=TS_HEIGHT
                    )

                    table.column('#1', width=TS_NUMBER_WIDTH)
                    table.heading('#1', text='№')

                    table.heading('#2', text='Назва предмету')

                    table.heading('#3', text='Вчитель')

                    table.column('#4', width=TS_TIME_WIDTH)
                    table.heading('#4', text='Час уроку')

                    scrollbar = tkinter.ttk.Scrollbar(
                        table_frame, orient=tkinter.VERTICAL, command=table.yview
                    )
                    table.configure(yscrollcommand=scrollbar.set)

                    table.pack(side=tkinter.LEFT)
                    scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

                    day_week = WEEKDAYS_DB[day]
                    for lesson in week[day_week]:
                        table.insert("", tkinter.END, values=lesson)

                    current_day += 1

    def show_groups_in_left_panel(self):
        left_panel = tkinter.Frame(self.main_window, bg=LE_PANEL_COLOR, width=LE_PANEL_WIDTH)

        self.num_class = tkinter.IntVar(value=OPTION_DEFAULT_VALUE)
        self.option_dictionary = dict()

        for i in range(CLASS_QUANTITY):
            option = tkinter.Radiobutton(left_panel, text=f'{i + 1} Клас', value=i + 1, bg=LE_PANEL_COLOR,
                                         fg=RB_FONT_COLOR,
                                         width=RB_WIDTH, variable=self.num_class,
                                         font=(RB_FONT, RB_FONT_SIZE, RB_FONT_FORMAT),
                                         command=self.controller.show_schedule)

            self.option_dictionary[i + 1] = option

            option.pack()

        left_panel.pack(side=tkinter.LEFT, fill=tkinter.Y)

    def create_schedule_frame(self, frame):
        if frame is not None:
            frame.destroy()

        return tkinter.Frame(self.main_window)

    def get_class_number(self):
        return self.num_class.get()
