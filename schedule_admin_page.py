import tkinter
from page import Page
from window_settings import (L_PANEL_COLOR, L_PANEL_WIDTH, L_PANEL_SIDE, L_PANEL_FILL, R_PANEL_SIDE,
                             RB_WIDTH, RB_FONT_COLOR, RB_FONT_SIZE, RB_FONT_FORMAT,
                             RB_FONT)


class Schedule(Page):
    def __init__(self, window):
        super().__init__(window)

    def show_left_panel(self):
        left_panel = tkinter.Frame(self.main_window, bg=L_PANEL_COLOR, width=L_PANEL_WIDTH)

        number_option = tkinter.IntVar(value=1)

        group_1 = tkinter.Radiobutton(left_panel, text="1 Клас", value=1, bg=L_PANEL_COLOR, fg=RB_FONT_COLOR, width=RB_WIDTH,
                                      font=(RB_FONT, RB_FONT_SIZE, RB_FONT_FORMAT), variable=number_option)
        group_2 = tkinter.Radiobutton(left_panel, text="2 Клас", value=2, bg=L_PANEL_COLOR, fg=RB_FONT_COLOR, width=RB_WIDTH,
                                      font=(RB_FONT, RB_FONT_SIZE, RB_FONT_FORMAT), variable=number_option)
        group_3 = tkinter.Radiobutton(left_panel, text="3 Клас", value=3, bg=L_PANEL_COLOR, fg=RB_FONT_COLOR, width=RB_WIDTH,
                                      font=(RB_FONT, RB_FONT_SIZE, RB_FONT_FORMAT), variable=number_option)
        group_4 = tkinter.Radiobutton(left_panel, text="4 Клас", value=4, bg=L_PANEL_COLOR, fg=RB_FONT_COLOR, width=RB_WIDTH,
                                      font=(RB_FONT, RB_FONT_SIZE, RB_FONT_FORMAT), variable=number_option)
        group_5 = tkinter.Radiobutton(left_panel, text="5 Клас", value=5, bg=L_PANEL_COLOR, fg=RB_FONT_COLOR, width=RB_WIDTH,
                                      font=(RB_FONT, RB_FONT_SIZE, RB_FONT_FORMAT), variable=number_option)
        group_6 = tkinter.Radiobutton(left_panel, text="6 Клас", value=6, bg=L_PANEL_COLOR, fg=RB_FONT_COLOR, width=RB_WIDTH,
                                      font=(RB_FONT, RB_FONT_SIZE, RB_FONT_FORMAT), variable=number_option)
        group_7 = tkinter.Radiobutton(left_panel, text="7 Клас", value=7, bg=L_PANEL_COLOR, fg=RB_FONT_COLOR, width=RB_WIDTH,
                                      font=(RB_FONT, RB_FONT_SIZE, RB_FONT_FORMAT), variable=number_option)
        group_8 = tkinter.Radiobutton(left_panel, text="8 Клас", value=8, bg=L_PANEL_COLOR, fg=RB_FONT_COLOR, width=RB_WIDTH,
                                      font=(RB_FONT, RB_FONT_SIZE, RB_FONT_FORMAT), variable=number_option)
        group_9 = tkinter.Radiobutton(left_panel, text="9 Клас", value=9, bg=L_PANEL_COLOR, fg=RB_FONT_COLOR, width=RB_WIDTH,
                                      font=(RB_FONT, RB_FONT_SIZE, RB_FONT_FORMAT), variable=number_option)
        group_10 = tkinter.Radiobutton(left_panel, text="10 Клас", value=1, bg=L_PANEL_COLOR, fg=RB_FONT_COLOR, width=RB_WIDTH,
                                       font=(RB_FONT, RB_FONT_SIZE, RB_FONT_FORMAT), variable=number_option)
        group_11 = tkinter.Radiobutton(left_panel, text="11 Клас", value=11, bg=L_PANEL_COLOR, fg=RB_FONT_COLOR, width=RB_WIDTH,
                                       font=(RB_FONT, RB_FONT_SIZE, RB_FONT_FORMAT), variable=number_option)

        left_panel.pack(side=L_PANEL_SIDE, fill=L_PANEL_FILL)

        group_1.pack()
        group_2.pack()
        group_3.pack()
        group_4.pack()
        group_5.pack()
        group_6.pack()
        group_7.pack()
        group_8.pack()
        group_9.pack()
        group_10.pack()
        group_11.pack()

        print(self.main_window.winfo_children())

    def show_main_panel(self):
        schedule = tkinter.Frame(self.main_window)

        monday_label = tkinter.Label(schedule, text="ПОНЕДІЛОК")

        schedule.pack()
        monday_label.pack(side=R_PANEL_SIDE)
