import tkinter.ttk
from page import Page
from window_settings import *
from test_data import *


class Schedule(Page):
    def __init__(self, window, controller):
        self.num_class = None
        super().__init__(window, controller)

    def __str__(self):
        return 'Schedule'

    def show_left_panel(self):
        self.show_groups_in_left_panel()

    def show_main_panel(self, data=None):

        schedule_frame = tkinter.Frame(
            self.main_window
        )
        schedule_frame.pack()

        week = data

        if week is not None:

            current_day = 0

            for i in range(TS_QUANTITY):

                column = tkinter.Frame(
                    schedule_frame
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
        left_panel = tkinter.Frame(self.main_window, bg=L_PANEL_COLOR, width=L_PANEL_WIDTH)

        self.num_class = tkinter.IntVar(value=0)

        for i in range(CLASS_QUANTITY):
            option = tkinter.Radiobutton(left_panel, text=f'{i + 1} Клас', value=i + 1, bg=L_PANEL_COLOR,
                                         fg=RB_FONT_COLOR,
                                         width=RB_WIDTH, variable=self.num_class,
                                         font=(RB_FONT, RB_FONT_SIZE, RB_FONT_FORMAT),
                                         command=self.controller.show_shedule)

            option.pack()

        left_panel.pack(side=tkinter.LEFT, fill=tkinter.Y)


    def get_class_number(self):
        return self.num_class.get()
