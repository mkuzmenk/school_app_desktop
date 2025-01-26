import tkinter
from page import Page
from window_settings import (L_PANEL_COLOR, L_PANEL_WIDTH, L_PANEL_SIDE, L_PANEL_FILL, R_PANEL_SIDE, RB_WIDTH,
                             RB_FONT_COLOR, RB_FONT_SIZE, RB_FONT_FORMAT, RB_FONT)


class Schedule(Page):
    def __init__(self, window):
        super().__init__(window)

    def show_left_panel(self):
        self.show_groups_in_left_panel()

    def show_main_panel(self):
        schedule = tkinter.Frame(self.main_window)

        monday_label = tkinter.Label(schedule, text="ПОНЕДІЛОК")

        schedule.pack()
        monday_label.pack(side=R_PANEL_SIDE)
