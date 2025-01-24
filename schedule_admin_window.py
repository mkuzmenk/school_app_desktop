import tkinter
from window_constants import PANEL_COLOR


class Schedule:
    def __init__(self, window):
        self.main_window = window

        self.__show_left_bar()

    def __del__(self):
        self.__hide_left_bar()

    def __show_left_bar(self):
        left_menu = tkinter.Frame(self.main_window, bg=PANEL_COLOR, width=200)

        schedule = tkinter.Frame(self.main_window)

        number_group = tkinter.IntVar(value=1)

        group_1 = tkinter.Radiobutton(left_menu, text="1 Клас", value=1, bg=PANEL_COLOR, fg="white", width=10,
                                      font=("Courier New", 18, "bold"), variable=number_group)
        group_2 = tkinter.Radiobutton(left_menu, text="2 Клас", value=2, bg=PANEL_COLOR, fg="white", width=10,
                                      font=("Courier New", 18, "bold"), variable=number_group)
        group_3 = tkinter.Radiobutton(left_menu, text="3 Клас", value=3, bg=PANEL_COLOR, fg="white", width=10,
                                      font=("Courier New", 18, "bold"), variable=number_group)
        group_4 = tkinter.Radiobutton(left_menu, text="4 Клас", value=4, bg=PANEL_COLOR, fg="white", width=10,
                                      font=("Courier New", 18, "bold"), variable=number_group)
        group_5 = tkinter.Radiobutton(left_menu, text="5 Клас", value=5, bg=PANEL_COLOR, fg="white", width=10,
                                      font=("Courier New", 18, "bold"), variable=number_group)
        group_6 = tkinter.Radiobutton(left_menu, text="6 Клас", value=6, bg=PANEL_COLOR, fg="white", width=10,
                                      font=("Courier New", 18, "bold"), variable=number_group)
        group_7 = tkinter.Radiobutton(left_menu, text="7 Клас", value=7, bg=PANEL_COLOR, fg="white", width=10,
                                      font=("Courier New", 18, "bold"), variable=number_group)
        group_8 = tkinter.Radiobutton(left_menu, text="8 Клас", value=8, bg=PANEL_COLOR, fg="white", width=10,
                                      font=("Courier New", 18, "bold"), variable=number_group)
        group_9 = tkinter.Radiobutton(left_menu, text="9 Клас", value=9, bg=PANEL_COLOR, fg="white", width=10,
                                      font=("Courier New", 18, "bold"), variable=number_group)
        group_10 = tkinter.Radiobutton(left_menu, text="10 Клас", value=1, bg=PANEL_COLOR, fg="white", width=10,
                                       font=("Courier New", 18, "bold"), variable=number_group)
        group_11 = tkinter.Radiobutton(left_menu, text="11 Клас", value=11, bg=PANEL_COLOR, fg="white", width=10,
                                       font=("Courier New", 18, "bold"), variable=number_group)

        monday_label = tkinter.Label(schedule, text="ПОНЕДІЛОК")

        left_menu.pack(side='left', fill='y')

        schedule.pack()

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

        monday_label.pack(side='right')

    def __hide_left_bar(self):
        for widget in self.main_window.winfo_children()[1:]:
            widget.destroy()
