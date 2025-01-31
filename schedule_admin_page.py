import tkinter.ttk
from page import Page
from window_settings import *
from test_data import *


class Schedule(Page):
    def __init__(self, window):
        super().__init__(window)

    def __str__(self):
        return 'Schedule'

    def show_left_panel(self):
        self.show_groups_in_left_panel()

    def show_main_panel(self):
        schedule_frame = tkinter.Frame(self.main_window)
        schedule_frame.pack()

        week = [SCHEDULE_LST_MON_1, SCHEDULE_LST_TUE_1, SCHEDULE_LST_WED_1, SCHEDULE_LST_THU_1, SCHEDULE_LST_FRI_1, SCHEDULE_LST_SAT_1]

        current_day = 0

        for i in range(T_QUANTITY):

            column = tkinter.Frame(schedule_frame)
            column.pack(side=tkinter.LEFT)

            for day in range(current_day, (len(week) // T_QUANTITY + current_day)):

                table_frame = tkinter.Frame(column)
                table_frame.pack()

                day_name = tkinter.Label(table_frame, text=WEEKDAYS[current_day],
                                         font=(R_PANEL_FONT, R_PANEL_FONT_SIZE))
                day_name.pack()

                table = tkinter.ttk.Treeview(table_frame, show='headings', columns=('#1', '#2', '#3', '#4'), height=T_HEIGHT)

                table.column('#1', width=T_NUMBER_WIDTH)
                table.heading('#1', text='№')

                table.heading('#2', text='Назва предмету')

                table.heading('#3', text='Вчитель')

                table.column('#4', width=T_TIME_WIDTH)
                table.heading('#4', text='Час уроку')

                scrollbar = tkinter.ttk.Scrollbar(table_frame, orient=tkinter.VERTICAL, command=table.yview)
                table.configure(yscrollcommand=scrollbar.set)

                table.pack(side='left')
                scrollbar.pack(side='right', fill='y')

                for lesson in week[day]:
                    table.insert("", tkinter.END, values=lesson)

                current_day += 1
